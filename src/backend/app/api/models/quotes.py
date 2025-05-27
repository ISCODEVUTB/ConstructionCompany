# filepath: /workspaces/ConstructionCompany/src/backend/app/api/models/cotizacion.py
from pydantic import BaseModel, Field
from typing import Optional

class Cotizacion(BaseModel):
    id: Optional[str] = Field(None, description="ID único de la cotización")
    cliente_id: str = Field(..., description="ID del cliente asociado a la cotización")
    total: float = Field(..., description="Monto total de la cotización")