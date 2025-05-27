from fastapi import APIRouter
from typing import List
from uuid import uuid4
from src.backend.app.api.models.clients import Cliente  # Importa el modelo desde models

router = APIRouter()

clientes_db: List[Cliente] = []

@router.post("/", status_code=201, response_model=Cliente)
def crear_cliente(cliente: Cliente):
    cliente.id = str(uuid4())
    clientes_db.append(cliente)
    return cliente