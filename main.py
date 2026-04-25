"""
Punto de entrada principal.
"""
import sys
import recursos_rc
from PySide6.QtWidgets import QApplication
from app.database.db import init_db
from app.models.cliente_repository import ClienteRepository
from app.views.main_window import MainWindow
from app.services.file_manager import (
    validar_estructura,
    verificar_año_clientes,
    sincronizar_plantillas_clientes,
)


def main():
    
    init_db()  # crea la base de datos con las tablas si no existen

    # Valida y crea las carpetas raíz si no existen
    for msg in validar_estructura():
        print(msg)

    # Obtiene todos los clientes para las validaciones de carpetas
    nombres_clientes = [c.nombre for c in ClienteRepository().get_all()]

    # Crea carpeta del año actual para clientes que no la tengan
    nuevos = verificar_año_clientes(nombres_clientes)
    if nuevos:
        print(f"Carpetas de año creadas para: {', '.join(nuevos)}")

    # Sincroniza copias de las plantillas 
    actualizadas = sincronizar_plantillas_clientes(nombres_clientes)
    if actualizadas:
        print(f"Plantillas sincronizadas: {len(actualizadas)}")

    app = QApplication(sys.argv)
    app.setApplicationName("MiApp")
    app.setApplicationVersion("1.0.0")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
