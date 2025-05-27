from pydantic import BaseModel
from typing import Optional

class Cliente(BaseModel):
    id: Optional[str] = None
    nombre: str
    documento: str