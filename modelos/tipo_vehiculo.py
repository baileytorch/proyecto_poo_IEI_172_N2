from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TipoVehiculo(Base):
    __tablename__ = 'tipos_vehiculo'
    id = Column(Integer, primary_key=True)
    tipo_vehiculo = Column(String(25), nullable=False)
    descripcion_tipo_vehiculo = Column(String(255), nullable=True)
