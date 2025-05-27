from fastapi import APIRouter
from typing import List
from src.backend.app.api.models.inventory import Inventario  # Importa el modelo desde models

router = APIRouter()

inventarios_db: List[Inventario] = []

@router.post("/registro")
def registrar_inventario(data: Inventario):
    inventarios_db.append(data)
    return {"mensaje": "Inventario registrado", "materiales": data.materiales}