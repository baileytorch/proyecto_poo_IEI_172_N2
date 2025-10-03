from auxiliares.info_app import nombre_aplicacion
from auxiliares.version import numero_version


def menu_principal():
    print()
    print(f'{nombre_aplicacion} {numero_version}')
    print('====================================')
    print('[1] Gestionar Animales')
    print('[2] Gestionar Personal')
    print('[3] Venta Entradas')
    print('[0] Salir')
