from fastapi import APIRouter, HTTPException
from typing import List
from uuid import uuid4
from backend.app.api.models.cotizacion import Cotizacion

router = APIRouter()

# Base de datos en memoria para cotizaciones
cotizaciones_db: List[Cotizacion] = []

@router.post("/", response_model=Cotizacion, status_code=201, summary="Crear cotización", description="Crea una nueva cotización con cliente y total.")
def crear_cotizacion(cotizacion: Cotizacion):
    cotizacion.id = str(uuid4())
    cotizaciones_db.append(cotizacion)
    return cotizacion

@router.get("/", response_model=List[Cotizacion], summary="Listar cotizaciones", description="Devuelve una lista de todas las cotizaciones registradas.")
def listar_cotizaciones():
    return cotizaciones_db

@router.get("/{cotizacion_id}", response_model=Cotizacion, summary="Obtener cotización", description="Obtiene una cotización específica por su ID.")
def obtener_cotizacion(cotizacion_id: str):
    for cotizacion in cotizaciones_db:
        if cotizacion.id == cotizacion_id:
            return cotizacion
    raise HTTPException(status_code=404, detail="Cotización no encontrada")

@router.delete("/{cotizacion_id}", status_code=204, summary="Eliminar cotización", description="Elimina una cotización por su ID.")
def eliminar_cotizacion(cotizacion_id: str):
    for i, cotizacion in enumerate(cotizaciones_db):
        if cotizacion.id == cotizacion_id:
            cotizaciones_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Cotización no encontrada")