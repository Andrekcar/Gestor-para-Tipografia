"""
Gestión de la estructura de carpetas del sistema

Jerarquía:
  Escritorio/
  ├── Plantillas Tipografia/        ← plantillas base
  └── Docs Tipografia/              ← carpetas de clientes
      └── {cliente}/
          └── {año}/
              └── {plantilla.cdr}   ← copia sincronizada 

Flujo:
  1. Al iniciar: validar_estructura() crea las carpetas si no existen.
  2. Al iniciar: verificar_año_clientes() crea la carpeta del año actual
     para cada cliente que aún no la tenga.
  3. Al iniciar: sincronizar_plantillas_clientes() actualiza copias cuya
     plantilla base haya cambiado
  4. Al crear cliente: crear_carpeta_cliente() crea {docs}/{cliente}/{año}/.
  5. Al guardar pedido con plantilla: copiar_plantilla() copia la plantilla
     base al año del cliente y retorna la ruta de la copia.
"""
import re
import shutil
from datetime import datetime
from pathlib import Path


ESCRITORIO=Path(r"C:\Users\Camilo Caro\OneDrive\Escritorio")
CARPETA_PLANTILLAS="Plantillas Tipografia"
CARPETA_DOCS="Docs Tipografia"


#Rutas derivadas
def ruta_plantillas() -> Path:
    #Carpeta raíz donde se guardan las plantillas base
    return ESCRITORIO / CARPETA_PLANTILLAS


def ruta_docs() -> Path:
    #Carpeta raíz donde se almacenan las carpetas de clientes
    return ESCRITORIO / CARPETA_DOCS


def ruta_cliente(nombre: str) -> Path:
    return ruta_docs() / _sanitizar(nombre)


def ruta_año_cliente(nombre: str, año: int | None = None) -> Path:
    # 
    return ruta_cliente(nombre) / str(año or datetime.now().year)


#Utilidades
def _sanitizar(nombre: str) -> str:
    #Elimina caracteres inválidos para nombres de carpeta en Windows
    return re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", nombre).strip(". ")


def _mas_reciente(origen: Path, destino: Path) -> bool:
    #True si origen tiene mtime más nuevo que destino
    return origen.stat().st_mtime > destino.stat().st_mtime


def validar_estructura() -> list[str]:
    #Verifica que las carpetas raíz existan y las crea si no.
    mensajes = []
    for ruta, nombre in [
        (ruta_plantillas(), CARPETA_PLANTILLAS),
        (ruta_docs(),       CARPETA_DOCS),
    ]:
        if not ruta.exists():
            ruta.mkdir(parents=True)
            mensajes.append(f"[CREADA] {ruta}")
        else:
            mensajes.append(f"[OK]     {ruta}")
    return mensajes


def crear_carpeta_cliente(nombre: str) -> Path:
    """Crea {docs}/{cliente}/{año_actual}/ al registrar un nuevo cliente.

    Usa exist_ok=True por si el cliente ya tenía carpeta previa.
    Retorna la ruta de la carpeta del año.
    """
    carpeta = ruta_año_cliente(nombre)
    carpeta.mkdir(parents=True, exist_ok=True)
    return carpeta


def verificar_año_clientes(nombres: list[str]) -> list[str]:
    """Crea la carpeta del año actual para cada cliente que aún no la tenga.

    Se llama al iniciar la app para manejar la transición de año: si el sistema
    detecta que el año cambió, todos los clientes reciben su nueva carpeta.
    Retorna la lista de nombres de clientes a los que se les creó la carpeta.
    """
    año   = datetime.now().year
    nuevos = []
    for nombre in nombres:
        carpeta = ruta_año_cliente(nombre, año)
        if not carpeta.exists():
            carpeta.mkdir(parents=True, exist_ok=True)
            nuevos.append(nombre)
    return nuevos


def _nombre_copia(cliente: str, tipo_trabajo: str, fecha: str, extension: str) -> str:
    """Construye el nombre del archivo copiado con la estructura:
    {cliente}_{tipo_trabajo}_{fecha}
    Sanitiza cada parte para que sea válida como nombre de archivo en Windows.
    """
    partes = [
        _sanitizar(cliente),
        _sanitizar(tipo_trabajo) if tipo_trabajo else "sin_tipo",
        _sanitizar(fecha),
    ]
    return "_".join(p for p in partes if p) + extension


def copiar_plantilla(nombre_cliente: str, ruta_base: str | Path, tipo_trabajo: str = "", fecha: str = "") -> Path | None:
    """Copia la plantilla al directorio {docs}/{cliente}/{año_actual}/.

    El archivo destino lleva el nombre {cliente}_{tipo_trabajo}_{fecha}{ext}
    Retorna la ruta de la copia
    """
    origen = Path(ruta_base)
    if not origen.exists():
        return None

    # Fecha hoy en formato YYYYMMDD
    fecha_str = fecha or datetime.now().strftime("%Y%m%d")

    nombre_destino = _nombre_copia(nombre_cliente, tipo_trabajo, fecha_str, origen.suffix)

    destino_dir = ruta_año_cliente(nombre_cliente)
    destino_dir.mkdir(parents=True, exist_ok=True)
    destino = destino_dir / nombre_destino

    # Si el origen ya ES la copia destino
    if origen.resolve() == destino.resolve():
        return destino

    shutil.copy2(str(origen), str(destino))
    return destino


def sincronizar_plantillas_clientes(nombres: list[str]) -> list[str]:
    """Recorre las copias de cada cliente y las actualiza si la plantilla base
    tiene mtime más nuevo (garantiza integridad tras editar una plantilla base).

    Retorna las rutas de los archivos que se actualizaron.
    """
    actualizadas: list[str] = []
    base = ruta_plantillas()
    if not base.exists():
        return actualizadas

    # Índice nombre→ruta de cada plantilla base
    base_idx = {p.name: p for p in base.iterdir() if p.is_file()}
    if not base_idx:
        return actualizadas

    for nombre in nombres:
        carpeta_cli = ruta_cliente(nombre)
        if not carpeta_cli.exists():
            continue
        # Recorre todas las subcarpetas de año
        for carpeta_año in sorted(carpeta_cli.iterdir()):
            if not carpeta_año.is_dir():
                continue
            for copia in carpeta_año.iterdir():
                if copia.name in base_idx and _mas_reciente(base_idx[copia.name], copia):
                    shutil.copy2(str(base_idx[copia.name]), str(copia))
                    actualizadas.append(str(copia))

    return actualizadas
