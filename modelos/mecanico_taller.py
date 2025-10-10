from sqlalchemy import Column, Integer, String, Date, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MecanicoTaller(Base):
    __tablename__ = 'mecanicos_taller'
    id = Column(Integer, primary_key=True)
    habilitado = Column(Boolean, default=True, nullable=False)
    id_mecanico = Column(Integer, nullable=False)
    id_taller = Column(Integer, nullable=False)
