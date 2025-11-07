from datos.conexion import Session
from sqlalchemy import func

sesion=Session()

def eliminar_objeto(objeto):
    sesion.merge(objeto)
    sesion.delete(objeto)
    try:
        sesion.commit()
        print("El objeto se ha elimnado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al eliminar el objeto: {e}")
    finally:
        sesion.close()