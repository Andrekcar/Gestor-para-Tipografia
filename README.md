# Gestor para Tipografía
Aplicación de escritorio para gestión de pedidos de diseño e impresión.
 
## Tecnologías
- Python
- PySide6
- SQLite

## Instalación manual
> Requiere tener **Python** y **Git** instalados en el sistema.

1. Clonar el repositorio

       git clone https://github.com/Andrekcar/Gestor-para-Tipografia.git

2. Crear entorno virtual

       python -m venv venv
       venv\Scripts\activate

3. Instalar dependencias

       pip install -r requirements.txt

4. Obtener la ruta del escritorio

Ejecutá el siguiente comando en tu CMD para obtener la ruta de tu escritorio (importante):

       echo %USERPROFILE%\Desktop

Copiá la ruta que aparece en pantalla, por ejemplo: C:\Users\user\Desktop

5. Configurar la ruta del escritorio

Abrí el archivo `file_manager.py` y en la **línea 28** reemplazá la ruta existente por la que obtuviste en el paso anterior:

       # línea 28 - file_manager.py
       ESCRITORIO=Path("C:/Users/USER1/Desktop")  # ← reemplazá con tu ruta

## Este paso manual es necesario dado que el software fue desarrollado **a medida para un equipo específico**, por lo que quedo fuera del alcance del proyecto implementar una función que detecte automáticamente la ruta del escritorio. Al tratarse de un entorno controlado y conocido, se optó por una ruta fija en lugar de una detección dinámica.

6. Ya puedes correr la app situandote en el archivo main.py
   

# Estructura del Proyecto — Gestor de Tipografía

```
Tipografia/
│
├── main.py                              # Punto de entrada: inicializa BD, carpetas, sincroniza plantillas y lanza la app Qt
├── lanzador.bat                         # Script Windows: clona el repo, crea el venv, instala dependencias y ejecuta main.py
├── requirements.txt                     # Dependencias del proyecto (PySide6 y shiboken6)
├── tipografia.db                        # Base de datos SQLite generada automáticamente al primer arranque
├── .gitignore                           # Archivos y carpetas excluidos del control de versiones
│
├── app/
│   │
│   ├── assets/                          # Recursos gráficos de la interfaz
│   │   ├── logo.png                     # Logo de la aplicación (icono de ventana y barra de tareas)
│   │   ├── coreldraw.png                # Icono del botón que abre archivos .cdr en CorelDraw
│   │   ├── pedido.png                   # Imagen decorativa para la sección de pedidos
│   │   └── nueva-cuenta.png             # Imagen decorativa para la sección de clientes
│   │
│   ├── database/
│   │   ├── __init__.py                  # Marca el directorio como paquete Python
│   │   └── db.py                        # Conexión SQLite y creación de tablas (clientes y pedidos)
│   │
│   ├── models/
│   │   ├── __init__.py                  # Marca el directorio como paquete Python
│   │   ├── cliente_repository.py        # Dataclass Cliente + CRUD completo sobre la tabla clientes
│   │   └── pedido_repository.py         # Dataclass Pedido + CRUD completo sobre la tabla pedidos
│   │
│   ├── services/
│   │   ├── __init__.py                  # Marca el directorio como paquete Python
│   │   └── file_manager.py              # Gestión de carpetas: crea estructura de directorios por cliente/año y sincroniza plantillas .cdr
│   │
│   └── views/
│       ├── main_window.py               # Ventana principal: tabla de pedidos, formulario, filtros, badges de estado y navegación
│       ├── clientes_main.py             # Vista de clientes: tabla, formulario y búsqueda de clientes
│       └── ui/
│           ├── ui_main_window.py        # Código Qt generado desde Qt Designer para la ventana principal
│           └── ui_clientes_page.py      # Código Qt generado desde Qt Designer para la página de clientes
│
└── venv/                                # Entorno virtual Python (no se versiona)
```
