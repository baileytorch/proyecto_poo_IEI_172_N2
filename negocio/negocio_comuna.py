from datos import obtener_lista_objetos, crear_objeto,modificar_objeto
from iu import str_nombre_comuna,str_codigo_comuna,str_nuevo_nombre_comuna,str_nuevo_codigo_comuna
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
    nombre = str_nombre_comuna()
    if nombre != '':
        comuna = obtener_comuna_nombre(nombre)
        if comuna == None:
            codigo = str_codigo_comuna()
            nueva_comuna = Comuna(
                nombre_comuna=nombre.title(),
                codigo_comuna=codigo)
            crear_objeto(nueva_comuna)
        else:
            print('Su comuna ya EXISTE.')

def modificar_comuna():
    nombre = str_nombre_comuna()
    if nombre != '':
        comuna = obtener_comuna_nombre(nombre)
        if comuna:
            modificar_nombre_comuna = str_nuevo_nombre_comuna()
            modificar_codigo_comuna = str_nuevo_codigo_comuna()
            if modificar_nombre_comuna!='':
                comuna.nombre_comuna = modificar_nombre_comuna
            if modificar_codigo_comuna!='':
                comuna.codigo_comuna = modificar_codigo_comuna
            modificar_objeto(comuna)
        else:
            print('No se ha encontrado la comuna.')