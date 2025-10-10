from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    rut_cliente = Column(String(10), nullable=False, unique=True)
    razon_social = Column(String(255), nullable=False)
    correo_contacto = Column(String(255), nullable=True)
    telefono_contacto = Column(String(12), nullable=True)
    habilitado = Column(Boolean, default=True, nullable=False)
    id_direccion = Column(Integer, nullable=True)
