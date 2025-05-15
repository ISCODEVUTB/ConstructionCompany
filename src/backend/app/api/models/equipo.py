from pydantic import BaseModel, Field
from typing import List, Optional

class Equipo(BaseModel):
    id: Optional[str] = Field(None, description="ID único del equipo")
    nombre: str = Field(..., description="Nombre del equipo")
    estado: str = Field(..., description="Estado actual del equipo (activo/inactivo)")
    ubicacion: str = Field(..., description="Ubicación del equipo")
    materiales: List[str] = Field(default=[], description="Lista de materiales asociados al equipo")