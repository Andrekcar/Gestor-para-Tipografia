# Gestor para Tipografía

Aplicación de escritorio para gestión de pedidos de diseño e impresión.

## Tecnologías
- Python
- PySide6
- SQLite

## Instalación

1. Clonar el repositorio
```bash
git clone https://github.com/Andrekcar/Gestor-para-Tipografia.git
```

2. Crear entorno virtual
```bash
python -m venv venv
venv\Scripts\activate
```

3. Instalar dependencias
```bash
pip install -r requirements.txt
```

## Uso
```bash
python main.py
```

## Estructura
```
📁 Gestor-para-Tipografia/
├── main.py
├── tipografia.db
├── .gitignore
├── app/
│   ├── assets/
│   │   └── coreldraw.png
│   ├── database/
│   │   ├── __init__.py
│   │   └── db.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── #
│   │   └── pedido_repository.py
│   └── views/
│       ├── ui/
│       │   ├── main_window.ui
│       │   └── ui_main_window.py
│       ├── #
│       └── main_window.py
```
