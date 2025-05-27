from pydantic import BaseModel
from typing import List

class Inventario(BaseModel):
    materiales: List[str]
    proyecto_id: int