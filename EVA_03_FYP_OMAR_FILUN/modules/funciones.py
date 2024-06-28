"""
En este archivo estarán las principales funciones para "app.py"
"""

import os
import json
import csv

tipos = ["acrilico", "latex"]
def listar(iterable):
    """
    Itera sobre una lista o diccionario
    """
    if iterable == []:
        print("El archivo está vacio\n")
    elif isinstance(iterable,list):
        for ind, op in enumerate(iterable):
            print(f"{ind+1}. {op}")
    elif isinstance(iterable,dict):
        for llave, valor in iterable.items():
            print(f"{llave.upper()} : {valor}")



def sol_ans():
    """
    Esta función pide una respuesta y la retorna
    """
    resp = input("¿Qué quieres hacer?:\n")
    return resp


def limpieza():
    """
    Limpía la pantalla
    """
    os.system("cls")



def no_valid():
    """
    Se usa cuando se ingresa una opción invalida
    """
    print("Ingresa una opción válida!\n")



def existencia(ruta):
    """
    Verifica si existe el archivo de la ruta
    ---PARAMS---
    ruta = debe ser una ruta hacia un archivo
    """
    if not ruta.exists():
        ruta.touch()
        print("La base no existía pero ha sido creada.\n")




def recuperar_data(ruta):
    """
    Esta función lee o recupera la data de un json
    ---PARAMS---
    ruta = debe ser una ruta válida hacia un json
    """
    if ruta == []:
        print("No hay nada para mostrar")
    elif ruta.stat().st_size == 0:
        print("El archivo está vacio")
    else:
        with open(ruta,"r") as stream:
            contenido = json.load(stream)
            return contenido
        


def mostrar_elementos(ruta):
    """
    Se encarga de listar los elementos del json
    ---PARAMS---
    ruta = debe ser una ruta válida hacia un json
    """
    contenido = recuperar_data(ruta)

    if contenido != []:
        listar(contenido)


def codigo(contenido):
    """
    se encarga de los codigo
    """
    if not contenido:
        return 380560
    else:
        codigo_nuevo = 380560 + 1
        return codigo_nuevo
def agregar(ruta):
    """
    Se encarga de agregar un elemento al json
    """
    contenido = recuperar_data(ruta)
    code = codigo(contenido)
    nombre  = input("Ingresa el nombre de la pintura(color): ")
    while True:
        print("Ingresa el tipo de pintura de la pintura a agregar")
        listar(tipos)
        resp = input(">")
        if resp == "1":
            for tipo in tipos:
                tipo == "acrilico"
                break
        elif resp == "2":
            for tipo in tipos:
                tipo == "latex"
                break
        else:
            print("Ingresa uno de los 2 tipos!\n")
        try:
            valor = int(input("Ingresa el valor de la pintura:\n"))
            break
        except ValueError:
            print("El precio debe ser numerico\n")
        try:
            stock = int(input("Ingresa el stock de la pintura:\n"))
            break
        except ValueError:
            print("El stock debe ser numerico\n")
        pintura = {
            "codigo": code,
            "nombre": nombre,
            "tipo" : tipo,
            "valor" : valor,
            "stock" : stock
        }
        with open(ruta,"w") as stream:
            json.dump(pintura,stream)
        print("Agregado exitosamente!\n")






##TERMINAR###
def buscar(ruta):
    """
    Se encarga de buscar por codigo o nombre
    ---PARAMS--
    ruta = debe ser una ruta válida hacia un json
    """
    contenido = recuperar_data(ruta)
    try:
        codigo = int(input("Ingresa codigo a buscar"))
    except ValueError:
        print("El codigo debe ser numerico\n")
    
    if codigo in contenido:
        for pintura in contenido:
            print([pintura])

    nombrebuscar = input("ingresa el nombre a borrar\n")
    if nombrebuscar in contenido:
        for nombrebuscar in contenido:
            print([pintura])




def export_csv(ruta):
    """
    exporta json a csv
    """
    existencia(ruta)
    contenido = recuperar_data(ruta)
    with open(ruta, mode='w', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(contenido)
        print("exportado!\n")


    


def eliminar(ruta):
    """
    elimina cosas del json
    """
    contenido = recuperar_data(ruta)
    if codigo in contenido:
        for pintura in contenido:
            del[pintura]
        print("la pintura fue eliminada\n")

    nombreborrar = input("ingresa el nombre a borrar\n")
    if nombreborrar in contenido:
        for nombreborrar in contenido:
            del[pintura]
        print("la pintura fue eliminada\n")