from datos.obtener_datos import obtener_lista_objetos
from modelos.marca import Marca


def obtener_marca_nombre(nombre: str):
    lista_marcas = obtener_lista_objetos(Marca)
    if lista_marcas:
        for marca in lista_marcas:
            if marca.nombre_marca == nombre.title():
                return marca
