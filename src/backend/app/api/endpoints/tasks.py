from fastapi import APIRouter, HTTPException
from typing import List
from uuid import uuid4
from src.backend.app.api.models.tasks import Tarea

router = APIRouter(tags=["tareas"])

tareas_db: List[Tarea] = []

@router.post("/", response_model=Tarea, status_code=201)
def crear_tarea(tarea: Tarea):
    tarea.id = str(uuid4())
    tareas_db.append(tarea)
    return tarea

@router.get("/", response_model=List[Tarea])
def listar_tareas():
    return tareas_db

@router.put("/{tarea_id}", response_model=Tarea)
def actualizar_tarea(tarea_id: str, datos: Tarea):
    for i, tarea in enumerate(tareas_db):
        if tarea.id == tarea_id:
            datos.id = tarea_id
            tareas_db[i] = datos
            return tareas_db[i]
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@router.delete("/{tarea_id}", status_code=204)
def eliminar_tarea(tarea_id: str):
    for i, tarea in enumerate(tareas_db):
        if tarea.id == tarea_id:
            tareas_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Tarea no encontrada")