from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    nombre: str
    email: str
    password: str
    rol: str
    id: Optional[str] = None