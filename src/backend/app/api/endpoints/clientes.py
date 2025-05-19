from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter()

class Cliente(BaseModel):
    nombre: str
    documento: str

clientes_db: List[Cliente] = []

@router.post("/", status_code=201)
def crear_cliente(cliente: Cliente):
    clientes_db.append(cliente)
    return cliente