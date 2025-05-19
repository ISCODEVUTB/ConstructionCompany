from fastapi import APIRouter, HTTPException
from typing import List
from uuid import uuid4
from backend.app.api.models.equipo import Equipo

router = APIRouter()

equipos_db: List[Equipo] = []

@router.post("/", response_model=Equipo, status_code=201)
def crear_equipo(equipo: Equipo):
    equipo.id = str(uuid4())
    equipos_db.append(equipo)
    return equipo

@router.get("/", response_model=List[Equipo])
def listar_equipos():
    return equipos_db

@router.get("/{equipo_id}", response_model=Equipo)
def obtener_equipo(equipo_id: str):
    for equipo in equipos_db:
        if equipo.id == equipo_id:
            return equipo
    raise HTTPException(status_code=404, detail="Equipo no encontrado")

@router.put("/{equipo_id}", response_model=Equipo)
def actualizar_equipo(equipo_id: str, datos: Equipo):
    for i, equipo in enumerate(equipos_db):
        if equipo.id == equipo_id:
            equipos_db[i] = datos.model_copy(update={"id": equipo_id})
            return equipos_db[i]
    raise HTTPException(status_code=404, detail="Equipo no encontrado")

@router.delete("/{equipo_id}", status_code=204)
def eliminar_equipo(equipo_id: str):
    for i, equipo in enumerate(equipos_db):
        if equipo.id == equipo_id:
            equipos_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Equipo no encontrado")