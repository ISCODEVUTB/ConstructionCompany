from pydantic import BaseModel
from typing import Optional
from datetime import date

class Pago(BaseModel):
    id: Optional[str] = None
    cliente_id: str
    monto: float
    fecha: date
    descripcion: Optional[str] = None