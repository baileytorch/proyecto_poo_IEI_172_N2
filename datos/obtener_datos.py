from datos.conexion import Session
from modelos.comuna import Comuna
from modelos.direccion import Direccion
from sqlalchemy import func

sesion = Session()


def obtener_lista_comunas():
    listado_comunas = sesion.query(Comuna).all()
    if len(listado_comunas) > 0:
        return listado_comunas
