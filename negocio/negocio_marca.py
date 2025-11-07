from datos import obtener_lista_objetos,crear_objeto,modificar_objeto,eliminar_objeto
from modelos.marca import Marca
from prettytable import PrettyTable
from iu import str_nombre_marca,str_pais_origen,str_nuevo_nombre_marca,str_nuevo_pais_origen

def obtener_listado_marcas():
    tabla_marcas = PrettyTable()
    tabla_marcas.field_names = ['N°', 'Nombre Marca', 'País de Origen']
    lista_marcas = obtener_lista_objetos(Marca)
    if lista_marcas:
        for marca in lista_marcas:
            tabla_marcas.add_row(
                [marca.id, marca.nombre_marca, marca.pais_origen])
    print(tabla_marcas)

def obtener_marca_nombre(nombre: str):
    lista_marcas = obtener_lista_objetos(Marca)
    if lista_marcas:
        for marca in lista_marcas:
            if marca.nombre_marca == nombre.title():
                return marca

def crear_marca():
    ingresar_nombre_marca = str_nombre_marca()
    if ingresar_nombre_marca != '':
        marca = obtener_marca_nombre(ingresar_nombre_marca)
        if marca == None:
            ingresar_pais_origen = str_pais_origen()
            nueva_marca = Marca(
                nombre_marca=ingresar_nombre_marca,
                pais_origen=ingresar_pais_origen.title())
            crear_objeto(nueva_marca)
        else:
            print('Su marca ya EXISTE.')

def modificar_marca():
    ingresar_nombre_marca = str_nombre_marca()
    if ingresar_nombre_marca != '':
        marca = obtener_marca_nombre(ingresar_nombre_marca)
        if marca:
            modificar_nombre_marca = str_nuevo_nombre_marca()
            modificar_pais_origen = str_nuevo_pais_origen()
            if modificar_nombre_marca!='':
                marca.nombre_marca = modificar_nombre_marca
            if modificar_pais_origen!='':
                marca.pais_origen = modificar_pais_origen
            modificar_objeto(marca)
        else:
            print('No se ha encontrado la marca.')

def eliminar_marca():
    ingresar_nombre_marca = str_nombre_marca()
    if ingresar_nombre_marca != '':
        marca = obtener_marca_nombre(ingresar_nombre_marca)
        if marca:
            eliminar_objeto(marca)
        else:
            print('No se ha encontrado la marca.')
