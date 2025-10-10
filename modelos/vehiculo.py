from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Vehiculo(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    anio_vehiculo = Column(String(4), nullable=False)
    patente_vehiculo = Column(String(7), nullable=False)
    color_vehiculo = Column(String(25), nullable=False)
    habilitado = Column(Boolean, default=True, nullable=False)
    modelo_vehiculo = Column(Integer, nullable=False)
    tipo_vehiculo = Column(Integer, nullable=False)
