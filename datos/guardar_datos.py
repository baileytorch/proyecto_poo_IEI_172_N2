from datos.conexion import Session
from sqlalchemy import func
from modelos import Marca, Modelo

sesion=Session()

def crear_objeto(objeto):
    sesion.add(objeto)
    try:
        sesion.commit()
        print("El objeto se ha guardado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al guardar el objeto: {e}")
    finally:
        sesion.close()

def modificar_objeto(objeto):
    sesion.merge(objeto)
    try:
        sesion.commit()
        print("El objeto se ha guardado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al guardar el objeto: {e}")
    finally:
        sesion.close()

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
