from datos.conexion import Session
from sqlalchemy import func

from modelos.comuna import Comuna

sesion = Session()


def obtener_lista_objetos(objeto):
    listado_objetos = sesion.query(objeto).all()
    if len(listado_objetos) > 0:
        return listado_objetos

def obtener_lista_comunas(filtro):
    busqueda = "%{}%".format(filtro)
    listado_objetos = sesion.query(Comuna).filter(Comuna.nombre_comuna.like(busqueda)).all()
    if len(listado_objetos) > 0:
        return listado_objetos