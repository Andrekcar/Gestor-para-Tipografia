# Gestor para Tipografía

Aplicación de escritorio para gestión de pedidos de diseño e impresión.

## Tecnologías
- Python
- PySide6
- SQLite

## Instalación rápida (Windows)

Descargá el archivo `lanzador.bat` y con un simple **doble clic**. El script automáticamente:
- Clona el repositorio
- Crea el entorno virtual
- Instala las dependencias
- Lanza la aplicación

> Puedes usar el lanzador repetidas veces, despues de la 1ra ejecución ya no se creara ni clonara nuevamente el proyecto y el entorno virtual, por lo puede usarse como lanzador principal
> Requiere tener **Python** y **Git** instalados en el sistema.

## Instalación manual

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
