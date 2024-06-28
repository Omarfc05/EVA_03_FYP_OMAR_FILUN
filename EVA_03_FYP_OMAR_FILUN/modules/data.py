"""
En este archivo se guardan rutas, datos y el menú principal para "app.py"
"""
from pathlib import Path

home = Path(__file__).parent
ruta_j = Path(home/"base.json")
ruta_c = Path(home/"mandarina.csv")

menup = ["Ver listado de pinturas", "Buscar Pintura", "Agregar Pintura", "Eliminar Pintura", "Exportar Pinturas a csv"]