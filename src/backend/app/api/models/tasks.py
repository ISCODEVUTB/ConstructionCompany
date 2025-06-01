from pydantic import BaseModel
from typing import Optional
from datetime import date

class Tarea(BaseModel):
    id: Optional[str] = None
    titulo: str
    descripcion: Optional[str] = None
    asignado_a: Optional[str] = None  # id del usuario o equipo
    fecha_limite: Optional[date] = None
    estado: Optional[str] = "pendiente"