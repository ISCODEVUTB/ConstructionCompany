from .config import Base, engine
from .models.equipo import Equipo

# Crear las tablas
Base.metadata.create_all(bind=engine)