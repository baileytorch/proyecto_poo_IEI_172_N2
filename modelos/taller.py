from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Taller(Base):
    __tablename__ = 'talleres'
    id = Column(Integer, primary_key=True)
    nombre_taller = Column(String(50), nullable=False)
    direccion_taller = Column(Integer, nullable=True)
    habilitado = Column(Boolean, default=True, nullable=False)
