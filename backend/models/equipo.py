# filepath: /workspaces/ConstructionCompany/backend/models/equipo.py
from sqlalchemy import Column, Integer, String
from ..config import Base

class Equipo(Base):
    __tablename__ = "equipos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String, nullable=True)

# filepath: /workspaces/ConstructionCompany/backend/init_db.py
from ..config import Base, engine
from .models.equipo import Equipo

# Crear las tablas
Base.metadata.create_all(bind=engine)

# filepath: /workspaces/ConstructionCompany/backend/routers/equipos.py
from fastapi import APIRouter, HTTPException
from typing import List
from ..models.equipo import Equipo

router = APIRouter()

# Base de datos simulada
equipos_db: List[Equipo] = []

# Crear equipo
@router.post("/equipos/", response_model=Equipo)
def crear_equipo(equipo: Equipo):
    equipos_db.append(equipo)
    return equipo

# Leer todos los equipos
@router.get("/equipos/", response_model=List[Equipo])
def obtener_equipos():
    return equipos_db

# Leer equipo por ID
@router.get("/equipos/{equipo_id}", response_model=Equipo)
def obtener_equipo(equipo_id: int):
    for equipo in equipos_db:
        if equipo.id == equipo_id:
            return equipo
    raise HTTPException(status_code=404, detail="Equipo no encontrado")

# Actualizar equipo
@router.put("/equipos/{equipo_id}", response_model=Equipo)
def actualizar_equipo(equipo_id: int, equipo_actualizado: Equipo):
    for index, equipo in enumerate(equipos_db):
        if equipo.id == equipo_id:
            equipos_db[index] = equipo_actualizado
            return equipo_actualizado
    raise HTTPException(status_code=404, detail="Equipo no encontrado")

# Eliminar equipo
@router.delete("/equipos/{equipo_id}")
def eliminar_equipo(equipo_id: int):
    for index, equipo in enumerate(equipos_db):
        if equipo.id == equipo_id:
            del equipos_db[index]
            return {"mensaje": "Equipo eliminado"}
    raise HTTPException(status_code=404, detail="Equipo no encontrado")

# filepath: /workspaces/ConstructionCompany/backend/app.py
from fastapi import FastAPI
from .routers import equipos

app = FastAPI()

# Incluir el router
app.include_router(equipos.router)

# filepath: /workspaces/ConstructionCompany/backend/config.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./equipos.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()