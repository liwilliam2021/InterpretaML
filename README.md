# InterpretaML
Herramientas de IA para detectar desinformación en Twitter y analizar datos sobre el Referéndum Constitucional

## Empezando

### Revisa tu versión de Python (solo ejecuta esto la primera vez)
`python --version`
Necesitas esta versión al menos 3.11 de Python. Si no, descárgalo [aquí](https://www.python.org/downloads/).

### Descargar paquetes (solo ejecuta esto la primera vez)
`./descargar_requisitos.sh`
Si tienes problemas de permiso
`chmod +x descargar_requisitos.sh`

### para usar GPT (solo ejecuta esto la primera vez)
`touch secret_key.py`
y después escribes el API key de Interpreta en el archivo 'secret_key.py'. Si no lo tienes, preguntas Will o tu jefe. 

### configurar paquetes (HAZ ESTO CADA VEZ QUE ABRAS)
`source venv/bin/activate`

### Generar Queries 
para ver una demostración
`python3 generar_query.py`

Si deseas hacer un query sobre un asunto X en el pais Y, debes ejecutar:
`python3 generar_query.py "X" "Y"`
El orden es importante, y necesitas encerrar en "", como:
`python3 generar_query.py "El Derecho del aborto" "Chile"`

### organización de archivos
##### conseguir_dato: para el scraper
Si el Twitter API cambie, el programa no funcionará
##### db: almacenamiento de datos
##### IA: modelos de IA
##### notebooks: código para experimentar

## Si tienes preguntas: willzli@stanford.edu, will@interpreta.org