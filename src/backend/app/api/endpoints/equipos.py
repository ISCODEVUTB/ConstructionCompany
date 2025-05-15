from fastapi import APIRouter, HTTPException
from backend.app.api.models.equipo import Equipo
from typing import List
from uuid import uuid4

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