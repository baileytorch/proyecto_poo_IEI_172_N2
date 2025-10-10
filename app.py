# from iu.menu_principal import menu_principal, seleccionar_opcion

# while True:
#     menu_principal()
#     seleccionar_opcion()
from modelos.comuna import Comuna
from modelos.marca import Marca
from datos.obtener_datos import obtener_lista_objetos


def trabajo_comunas():
    comuna = Comuna
    listado_comunas = obtener_lista_objetos(comuna)
    if listado_comunas:
        for comuna in listado_comunas:
            print(f'{comuna.id} {comuna.codigo_comuna} {comuna.nombre_comuna}')


def trabajo_marcas():
    marca = Marca
    listado_marcas = obtener_lista_objetos(marca)
    if listado_marcas:
        for marca in listado_marcas:
            print(f'{marca.id} {marca.nombre_marca} {marca.pais_origen}')


trabajo_marcas()
