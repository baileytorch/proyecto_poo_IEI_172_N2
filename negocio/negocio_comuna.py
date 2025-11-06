from datos import obtener_lista_objetos, crear_objeto
from iu import datos_comuna
from modelos import Comuna
from prettytable import PrettyTable


def obtener_listado_comunas():
    tabla_comunas = PrettyTable()
    tabla_comunas.field_names = ['N°', 'Código Comuna', 'Nombre Comuna']
    lista_comunas = obtener_lista_objetos(Comuna)
    if lista_comunas:
        for comuna in lista_comunas:
            tabla_comunas.add_row(
                [comuna.id, comuna.codigo_comuna, comuna.nombre_comuna])
    print(tabla_comunas)


def obtener_comuna_nombre(nombre: str):
    lista_comunas = obtener_lista_objetos(Comuna)
    if lista_comunas:
        for comuna in lista_comunas:
            if comuna.nombre_comuna == nombre.title():
                return comuna


def crear_comuna():
    nombre, codigo = datos_comuna()
    if nombre!='':
        comuna = obtener_comuna_nombre(nombre)
        if comuna==None:
            nueva_comuna = Comuna(
                nombre_comuna=nombre.title(),
                codigo_comuna=codigo)
            crear_objeto(nueva_comuna)
        else:
            print('Su comuna ya EXISTE.')
