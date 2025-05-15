# filepath: /workspaces/ConstructionCompany/src/backend/app/api/models/proyecto.py
from pydantic import BaseModel, Field
from typing import List, Optional
from api.models.equipo import Equipo

class Proyecto(BaseModel):
    id: Optional[str] = Field(None, description="ID único del proyecto")
    nombre: str = Field(..., description="Nombre del proyecto")
    descripcion: str = Field(..., description="Descripción del proyecto")
    estado: str = Field(..., description="Estado actual del proyecto")
    fecha_inicio: str = Field(..., description="Fecha de inicio del proyecto")
    fecha_fin: Optional[str] = Field(None, description="Fecha de finalización del proyecto")
    materiales: List[str] = Field(default_factory=list, description="Lista de materiales asociados al proyecto")
    equipos: List[Equipo] = Field(default_factory=list, description="Lista de equipos asignados al proyecto")