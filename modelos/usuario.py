from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(50), nullable=True)
    contrasena_usuario = Column(String(50), nullable=True)
    habilitado = Column(Boolean, default=True, nullable=False)
    id_mecanico = Column(Integer, nullable=False)
