from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter()

class Inventario(BaseModel):
    materiales: List[str]
    proyecto_id: int

inventarios_db: List[Inventario] = []

@router.post("/registro")
def registrar_inventario(data: Inventario):
    inventarios_db.append(data)
    return {"mensaje": "Inventario registrado", "materiales": data.materiales}