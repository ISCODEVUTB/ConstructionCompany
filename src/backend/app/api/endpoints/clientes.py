from fastapi import APIRouter
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

router = APIRouter()

class Cliente(BaseModel):
    id: Optional[str] = None
    nombre: str
    documento: str

clientes_db: List[Cliente] = []

@router.post("/", status_code=201, response_model=Cliente)
def crear_cliente(cliente: Cliente):
    cliente.id = str(uuid4())
    clientes_db.append(cliente)
    return cliente