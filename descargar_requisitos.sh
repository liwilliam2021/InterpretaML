#!/bin/bash

VIRTUALENV_PATH="./venv"
DIRECTORY="."

# Verifica si el virtual environment existe, si no, créalo
if [ ! -d "$VIRTUALENV_PATH" ]; then
    echo "Virtual environment no encontrado. Creando uno en $VIRTUALENV_PATH"
    python3 -m venv "$VIRTUALENV_PATH"
fi

# Activa el virtual environment
source "$VIRTUALENV_PATH/bin/activate"

# Encuentra todos los archivos requirements.txt e instálalos
find "$DIRECTORY" -name 'requirements.txt' | while read -r file; do
    echo "Instalando requisitos desde: $file"
    pip install -r "$file" || {
        echo "Fallo al instalar requisitos desde $file"
        exit 1
    }
done

echo "Todos los requisitos se instalaron exitosamente."

# Desactiva the virtual environment
deactivate