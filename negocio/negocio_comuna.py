from datos.obtener_datos import obtener_lista_objetos
from modelos.comuna import Comuna


def obtener_comuna_nombre(nombre: str):
    lista_comunas = obtener_lista_objetos(Comuna)
    if lista_comunas:
        for comuna in lista_comunas:
            if comuna.nombre_comuna == nombre.title():
                return comuna
