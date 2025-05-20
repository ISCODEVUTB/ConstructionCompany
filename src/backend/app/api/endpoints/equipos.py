from fastapi import APIRouter, HTTPException, Depends, Header, status
from typing import List
from uuid import uuid4
from backend.app.api.models.equipo import Equipo
from backend.app.api.endpoints.auth import verificar_token

router = APIRouter(prefix="/registro-equipos/equipos", tags=["equipos"])

equipos_db: List[Equipo] = []

@router.post(
    "/",
    response_model=Equipo,
    status_code=status.HTTP_201_CREATED,
    summary="Crear nuevo equipo",
    dependencies=[Depends(verificar_token)]
)
def crear_equipo(equipo: Equipo):
    equipo.id = str(uuid4())
    equipos_db.append(equipo)
    return equipo

@router.get(
    "/",
    response_model=List[Equipo],
    summary="Listar todos los equipos",
    dependencies=[Depends(verificar_token)]
)
def listar_equipos():
    return equipos_db

@router.get(
    "/{equipo_id}",
    response_model=Equipo,
    summary="Obtener equipo por ID",
    dependencies=[Depends(verificar_token)]
)
def obtener_equipo(equipo_id: str):
    equipo = next((e for e in equipos_db if e.id == equipo_id), None)
    if not equipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Equipo no encontrado"
        )
    return equipo

@router.put(
    "/{equipo_id}",
    response_model=Equipo,
    summary="Actualizar equipo",
    dependencies=[Depends(verificar_token)]
)
def actualizar_equipo(equipo_id: str, datos: Equipo):
    for i, equipo in enumerate(equipos_db):
        if equipo.id == equipo_id:
            datos.id = equipo_id  # Mantener el mismo ID
            equipos_db[i] = datos
            return equipos_db[i]
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Equipo no encontrado"
    )

@router.delete(
    "/{equipo_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar equipo",
    dependencies=[Depends(verificar_token)]
)
def eliminar_equipo(equipo_id: str):
    for i, equipo in enumerate(equipos_db):
        if equipo.id == equipo_id:
            equipos_db.pop(i)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Equipo no encontrado"
    )