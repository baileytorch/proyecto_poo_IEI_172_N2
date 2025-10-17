from datos.conexion import Session
from sqlalchemy import func
from modelos.comuna import Comuna
from modelos.marca import Marca
from modelos.modelo import Modelo

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


def guardar_marca(marca, pais):
    if marca != '':
        nueva_marca = Marca(
            nombre_marca=marca,
            pais_origen=pais.title())
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
    else:
        print('Debe ingresar el nombre de la marca.')


def guardar_modelo(modelo, descripcion, combustible, cant_puertas, marca):
    nuevo_modelo = Modelo(
        nombre_modelo=modelo,
        descripcion_modelo=descripcion,
        tipo_combustible=combustible,
        puertas=cant_puertas,
        id_marca=marca)
    sesion.add(nuevo_modelo)
    try:
        sesion.commit()
        print(
            f"La marca '{nuevo_modelo.nombre_marca}' se ha guardado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al guardar la marca: {e}")
    finally:
        sesion.close()
