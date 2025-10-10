from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Direccion(Base):
    __tablename__ = 'direcciones'
    id = Column(Integer, primary_key=True)
    calle = Column(String(255), nullable=True)
    numero = Column(String(10), nullable=True)
    departamento = Column(String(10), nullable=True)
    detalles = Column(String(255), nullable=True)
    id_comuna = Column(Integer, nullable=False)
