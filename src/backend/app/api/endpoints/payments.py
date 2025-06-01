from fastapi import APIRouter, HTTPException
from typing import List
from uuid import uuid4
from src.backend.app.api.models.payments import Pago

router = APIRouter(tags=["pagos"])

pagos_db: List[Pago] = []

@router.post("/", response_model=Pago, status_code=201)
def registrar_pago(pago: Pago):
    pago.id = str(uuid4())
    pagos_db.append(pago)
    return pago

@router.get("/", response_model=List[Pago])
def listar_pagos():
    return pagos_db