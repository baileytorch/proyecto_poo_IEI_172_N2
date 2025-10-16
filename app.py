# from iu.menu_principal import menu_principal, seleccionar_opcion

# while True:
#     menu_principal()
#     seleccionar_opcion()
from modelos.comuna import Comuna
from modelos.marca import Marca
from datos.obtener_datos import obtener_lista_objetos
from datos.guardar_datos import guardar_marca
from negocio.negocio_marca import obtener_marca_nombre
from negocio.negocio_comuna import obtener_comuna_nombre

from prettytable import PrettyTable


def trabajo_comunas():
    tabla_comunas = PrettyTable()
    tabla_comunas.field_names = ['N°', 'Código Comuna', 'Nombre Comuna']
    comuna = Comuna
    listado_comunas = obtener_lista_objetos(comuna)
    if listado_comunas:
        for comuna in listado_comunas:
            tabla_comunas.add_row(
                [comuna.id, comuna.codigo_comuna, comuna.nombre_comuna])
            # print(f'{comuna.id} {comuna.codigo_comuna} {comuna.nombre_comuna}')
        print(tabla_comunas)


def trabajo_marcas():
    tabla_marcas = PrettyTable()
    tabla_marcas.field_names = ['N°', 'Marca', 'País Origen']
    marca = Marca
    listado_marcas = obtener_lista_objetos(marca)
    if listado_marcas:
        for marca in listado_marcas:
            tabla_marcas.add_row(
                [marca.id, marca.nombre_marca, marca.pais_origen])
            # print(f'{marca.id} {marca.nombre_marca} {marca.pais_origen}')
        print(tabla_marcas)


def buscar_marca():
    tabla = PrettyTable()
    tabla.field_names = ['N°', 'Marca', 'País Origen']
    nombre_marca = input('Ingrese nombre de marca a buscar: ')
    if nombre_marca != '':
        marca = obtener_marca_nombre(nombre_marca)
        if marca is not None:
            tabla.add_row(
                [marca.id, marca.nombre_marca, marca.pais_origen])
            print(tabla)


def buscar_comuna():
    tabla = PrettyTable()
    tabla.field_names = ['N°', 'Código Comuna', 'Nombre Comuna']
    nombre_comuna = input('Ingrese nombre de comuna a buscar: ')
    if nombre_comuna != '':
        comuna = obtener_comuna_nombre(nombre_comuna)
        if comuna is not None:
            tabla.add_row(
                [comuna.id, comuna.codigo_comuna, comuna.nombre_comuna])
            print(tabla)


# trabajo_comunas()
# trabajo_marcas()
# buscar_marca()
# buscar_comuna()
guardar_marca()
