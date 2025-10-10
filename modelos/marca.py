from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Marca(Base):
    __tablename__ = 'marcas'
    id = Column(Integer, primary_key=True)
    nombre_marca = Column(String(25), nullable=False)
    pais_origen = Column(String(50), nullable=True)
