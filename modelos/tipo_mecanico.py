from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TipoMecanico(Base):
    __tablename__ = 'tipos_mecanico'
    id = Column(Integer, primary_key=True)
    tipo_mecanico = Column(String(50), nullable=False)
    descripcion_tipo_mecanico = Column(String(255), nullable=True)
    habilitado = Column(Boolean, default=True, nullable=False)
