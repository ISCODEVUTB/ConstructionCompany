from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    id: str | None = None
    nombre: str
    email: str
    password: str
    rol: str = "usuario"  # valor por defecto

    class Config:
        orm_mode = True