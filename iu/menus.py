from auxiliares.info_app import nombre_aplicacion
from auxiliares.version import numero_version


def menu_principal():
    print()
    print(f'{nombre_aplicacion} {numero_version}')
    print('====================================')
    print('[1] Gestionar Talleres.')
    print('[2] Gestionar Personal.')
    print('[3] Gestionar Clientes.')
    print('[4] Gestionar Trabajos.')
    print('[0] Salir')


def menu_trabajos():
    print('====================================')
    print('[1] Ver listado de trabajos pendientes.')
    print('[2] Ver listado de trabajos finalizados.')
    print('[3] Ingresar nuevo trabajo.')
    print('[4] Modificar trabajo.')
    print('[0] Volver')
