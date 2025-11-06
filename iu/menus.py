# Definición de constantes literales para menú
separador_menu = '===================================='
opcion_volver = '[0] Volver'


def menu_principal():
    print()
    print(separador_menu)
    print('Menú Principal')
    print(separador_menu)
    print('[1] Gestionar Talleres.')
    print('[2] Gestionar Personal.')
    print('[3] Gestionar Clientes.')
    print('[4] Gestionar Trabajos.')
    print('[5] Configuración Aplicación.')
    print('[0] Salir')


def menu_trabajos():
    print()
    print(separador_menu)
    print('Menú Trabajos')
    print(separador_menu)
    print('[1] Ver listado de trabajos pendientes.')
    print('[2] Ver listado de trabajos finalizados.')
    print('[3] Ingresar nuevo trabajo.')
    print('[4] Modificar trabajo.')
    print(opcion_volver)


def menu_configuracion():
    print()
    print(separador_menu)
    print('Menú Configuración Aplicación')
    print(separador_menu)
    print('[1] Gestion Comunas.')
    print('[2] Horarios Taller.')
    print('[3] Gestión Proveedores.')
    print('[4] Gestión Repuestos.')
    print(opcion_volver)


def sub_menu_comunas():
    print()
    print(separador_menu)
    print('Sub-Menú Gestión Comunas')
    print(separador_menu)
    print('[1] Listado Comunas.')
    print('[2] Agregar Comuna.')
    print('[3] Modificar Comuna.')
    print('[4] Eliminar Comuna.')
    print(opcion_volver)
    
