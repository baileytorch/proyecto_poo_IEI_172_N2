from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Reparacion(Base):
    __tablename__ = 'reparaciones'
    id = Column(Integer, primary_key=True)
    motivo_ingreso = Column(String(255), nullable=False)
    fecha_ingreso = Column(DateTime(timezone=True), server_default=func.now())
    fecha_entrega = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
