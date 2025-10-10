from auxiliares.info_app import nombre_aplicacion
from auxiliares.version import numero_version

from modelos.comuna import Comuna
from datos.obtener_datos import obtener_lista_datos


def menu_principal():
    print()
    print(f'{nombre_aplicacion} {numero_version}')
    print('====================================')
    print('[1] Gestionar Talleres')
    print('[2] Gestionar Personal')
    print('[3] Gestionar Clientes')
    print('[4] Gestionar Trabajos')
    print('[5] Gestionar Comunas')
    print('[0] Salir')


def seleccionar_opcion():
    opcion = input('Seleccione su opción [0-5]: ')

    if opcion == '1':
        pass
    elif opcion == '2':
        pass
    elif opcion == '5':
        listado_comunas = obtener_lista_datos('comuna')
        if len(listado_comunas) > 0:
            for comuna in listado_comunas:
                print(f'{comuna.id} {comuna.codigo_comuna} {comuna.nombre_comuna}')
