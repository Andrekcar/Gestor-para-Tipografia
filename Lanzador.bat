@echo off

if not exist "Gestor-para-Tipografia" (
    echo Clonando repositorio...
    git clone https://github.com/Andrekcar/Gestor-para-Tipografia.git
    cd Gestor-para-Tipografia
    echo Creando entorno virtual...
    python -m venv venv
    echo Instalando dependencias...
    call venv\Scripts\activate
    pip install -r requirements.txt
) else (
    echo Repositorio ya existe, activando entorno...
    cd Gestor-para-Tipografia
    call venv\Scripts\activate
)

echo Lanzando aplicacion...
python main.py
pause