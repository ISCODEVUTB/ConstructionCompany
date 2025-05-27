from fastapi import APIRouter, HTTPException
from typing import List
from uuid import uuid4
from src.backend.app.api.models.projects import Proyecto

router = APIRouter()

# Base de datos en memoria para proyectos
proyectos_db: List[Proyecto] = []

@router.post("/", response_model=Proyecto, status_code=201, summary="Crear proyecto", description="Crea un nuevo proyecto y lo agrega a la base de datos.")
def crear_proyecto(proyecto: Proyecto):
    proyecto.id = str(uuid4())
    proyectos_db.append(proyecto)
    return proyecto

@router.get("/", response_model=List[Proyecto], summary="Listar proyectos", description="Devuelve una lista de todos los proyectos registrados.")
def listar_proyectos():
    return proyectos_db

@router.get("/{proyecto_id}", response_model=Proyecto, summary="Obtener proyecto", description="Obtiene un proyecto específico por su ID.")
def obtener_proyecto(proyecto_id: str):
    for proyecto in proyectos_db:
        if proyecto.id == proyecto_id:
            return proyecto
    raise HTTPException(status_code=404, detail="Proyecto no encontrado")

@router.put("/{proyecto_id}", response_model=Proyecto, summary="Actualizar proyecto", description="Actualiza los datos de un proyecto existente.")
def actualizar_proyecto(proyecto_id: str, datos: Proyecto):
    for i, proyecto in enumerate(proyectos_db):
        if proyecto.id == proyecto_id:
            # Asegura que el id no se pierda al actualizar
            datos.id = proyecto_id
            proyectos_db[i] = datos
            return proyectos_db[i]
    raise HTTPException(status_code=404, detail="Proyecto no encontrado")

@router.delete("/{proyecto_id}", status_code=204, summary="Eliminar proyecto", description="Elimina un proyecto por su ID.")
def eliminar_proyecto(proyecto_id: str):
    for i, proyecto in enumerate(proyectos_db):
        if proyecto.id == proyecto_id:
            proyectos_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Proyecto no encontrado")