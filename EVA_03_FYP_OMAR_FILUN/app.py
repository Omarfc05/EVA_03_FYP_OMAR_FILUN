"""
Este es el archivo principal.
Se encarga del stock de Pinturas Acrilicas Mandarina
Recibe funciones de "funciones.py" y datos de "data.py"
"""

from modules.funciones import *
from modules.data import *


#Comienza el control de flujo

while True:
    listar(menup)
    ans = sol_ans()
    limpieza()
    if ans == "1":
        existencia(ruta_j)
        mostrar_elementos(ruta_j)
    elif ans == "2":
        buscar()
    elif ans == "3":
        existencia(ruta_j)
        agregar(ruta_j)
    elif ans == "4":
        eliminar()
    elif ans == "5":
        export_csv()
    else:
        no_valid()