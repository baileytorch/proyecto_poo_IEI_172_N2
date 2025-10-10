from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Comuna(Base):
    __tablename__ = 'comunas'
    id = Column(Integer, primary_key=True)
    codigo_comuna = Column(String(5), nullable=False)
    nombre_comuna = Column(String(60), nullable=False)
