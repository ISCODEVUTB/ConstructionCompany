from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    id: Optional[str] = None
    nombre: str
    email: str
    rol: Optional[str] = "usuario"