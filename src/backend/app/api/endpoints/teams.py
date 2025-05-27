from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from uuid import uuid4
from backend.app.api.endpoints.auth import get_current_user
from src.backend.app.api.models.teams import Equipo

router = APIRouter(tags=["equipos"])

equipos_db: List[Equipo] = []

@router.post("/", response_model=Equipo, status_code=201)
async def crear_equipo(equipo: Equipo, current_user: dict = Depends(get_current_user)):
    equipo.id = str(uuid4())
    equipos_db.append(equipo)
    return equipo

@router.get("/", response_model=List[Equipo], summary="Listar todos los equipos")
async def listar_equipos(current_user: dict = Depends(get_current_user)):
    return equipos_db

@router.get("/{equipo_id}", response_model=Equipo, summary="Obtener equipo por ID")
async def obtener_equipo(equipo_id: str, current_user: dict = Depends(get_current_user)):
    equipo = next((e for e in equipos_db if e.id == equipo_id), None)
    if not equipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Equipo no encontrado"
        )
    return equipo

@router.put("/{equipo_id}", response_model=Equipo, summary="Actualizar equipo")
async def actualizar_equipo(equipo_id: str, datos: Equipo, current_user: dict = Depends(get_current_user)):
    for i, equipo in enumerate(equipos_db):
        if equipo.id == equipo_id:
            datos.id = equipo_id
            equipos_db[i] = datos
            return equipos_db[i]
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Equipo no encontrado"
    )

@router.delete("/{equipo_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar equipo")
async def eliminar_equipo(equipo_id: str, current_user: dict = Depends(get_current_user)):
    for i, equipo in enumerate(equipos_db):
        if equipo.id == equipo_id:
            equipos_db.pop(i)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Equipo no encontrado"
    )