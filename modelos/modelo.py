from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Modelo(Base):
    __tablename__ = 'modelos'
    id = Column(Integer, primary_key=True)
    nombre_modelo = Column(String(25), nullable=False)
    descripcion_modelo = Column(String(255), nullable=True)
    tipo_combustible = Column(Integer, nullable=False)
    puertas = Column(Integer, nullable=False)
