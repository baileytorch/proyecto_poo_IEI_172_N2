from datos.conexion import Session
from sqlalchemy import func
from modelos.comuna import Comuna
from modelos.marca import Marca

sesion = Session()


def guardar_comuna():
    nombre = input('Ingrese nombre comuna: ')
    codigo = input('Ingrese código de comuna: ')
    nueva_comuna = Comuna(
        nombre_comuna=nombre.title(),
        codigo_comuna=codigo)
    sesion.add(nueva_comuna)
    try:
        sesion.commit()
        print(
            f"La comuna '{nueva_comuna.nombre_marca}' se ha guardado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al guardar la comuna: {e}")
    finally:
        sesion.close()


def guardar_marca():
    nombre = input('Ingrese nombre marca: ')
    pais = input('Ingrese país de origen: ')
    nueva_marca = Marca(nombre_marca=nombre.title(), pais_origen=pais.title())
    sesion.add(nueva_marca)
    try:
        sesion.commit()
        print(
            f"La marca '{nueva_marca.nombre_marca}' se ha guardado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al guardar la marca: {e}")
    finally:
        sesion.close()


# def guardar_modelo():
#     nombre = input('Ingrese nombre marca: ')
#     marca = obtener_marca_nombre(nombre)
#     if not marca:
#         guardar_marca()
#     modelo = input('Ingrese nombre del modelo: ')
#     descripcion = input('Ingrese descripción del modelo: ')
#     tipo_combustible = input('Ingrese tipo de combustible: ')
#     combustible = obtener_combustible_nombre(tipo_combustible)
#     nuevo_modelo = Modelo(
#         nombre_modelo=modelo.title(),
#         descripcion_modelo=descripcion.title())
#     sesion.add(nuevo_modelo)
#     try:
#         sesion.commit()
#         print(
#             f"La marca '{nuevo_modelo.nombre_marca}' se ha guardado correctamente.")
#     except Exception as e:
#         sesion.rollback()
#         print(f"Error al guardar la marca: {e}")
#     finally:
#         sesion.close()
