def datos_comuna():
    nombre = input('Ingrese nombre comuna: ')
    codigo = input('Ingrese código de comuna: ')
    return nombre.title(), codigo

def datos_marca():
    nombre = input('Ingrese nombre marca: ')
    pais = input('Ingrese país de origen: ')
    return nombre, pais.title()