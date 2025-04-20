from .config import Base, engine
from backend.models.equipo import Equipo

# Crear las tablas
Base.metadata.create_all(bind=engine)