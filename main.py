"""
Punto de entrada principal.
"""
import sys # para sys.argv y sys.exit
from PySide6.QtWidgets import QApplication # para crear la aplicación Qt
from app.database.db import init_db # para inicializar la base de datos
from app.views.main_window import MainWindow # para importar la ventana principal de la aplicación

def main():
    
    init_db() # crea tipografia.db y las tablas si no existen
    app = QApplication(sys.argv) 
    app.setApplicationName("MiApp")
    app.setApplicationVersion("1.0.0")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
