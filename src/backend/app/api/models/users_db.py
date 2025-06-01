from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UsuarioDB(Base):
    __tablename__ = "usuarios"
    id = Column(String(36), primary_key=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    rol = Column(String(50), nullable=False)