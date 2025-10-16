from datos.obtener_datos import obtener_lista_objetos
from modelos.combustible import Combustible


def obtener_combustible_nombre(nombre: str):
    lista_combustibles = obtener_lista_objetos(Combustible)
    if lista_combustibles:
        for combustible in lista_combustibles:
            if combustible.tipo_combustible == nombre.title():
                return combustible
