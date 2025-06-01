from pydantic import BaseModel
from typing import Optional

class Pago(BaseModel):
    monto: float
    fecha: str
    metodo: str
    descripcion: str
    id: Optional[str] = None