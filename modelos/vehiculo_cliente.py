from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class VehiculoCliente(Base):
    __tablename__ = 'vehiculos_cliente'
    id = Column(Integer, primary_key=True)
    id_vehiculo = Column(Integer, nullable=False)
    id_cliente = Column(Integer, nullable=False)
    id_taller = Column(Integer, nullable=False)
