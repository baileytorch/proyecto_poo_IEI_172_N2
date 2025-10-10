from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Combustible(Base):
    __tablename__ = 'combustibles'
    id = Column(Integer, primary_key=True)
    tipo_combustible = Column(String(25), nullable=False)
    descripcion_tipo_combustible = Column(String(255), nullable=True)
