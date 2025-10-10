from sqlalchemy import Column, Integer, String, Date, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Mecanico(Base):
    __tablename__ = 'mecanicos'
    id = Column(Integer, primary_key=True)
    rut_mecanico = Column(String(10), nullable=False, unique=True)
    nombre_mecanico = Column(String(100), nullable=False)
    fecha_contrato = Column(Date, nullable=False)
    salario_mecanico = Column(Float, nullable=True)
    telefono_mecanico = Column(String(12), nullable=True)
    fecha_nacimiento_mecanico = Column(Date, nullable=True)
    habilitado = Column(Boolean, default=True, nullable=False)
    tipo_mecanico = Column(Integer, nullable=False)
    direccion_mecanico = Column(Integer, nullable=True)
