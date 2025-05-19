from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    usuario: str
    password: str

@router.post("/", summary="Iniciar sesión", description="Permite a un usuario iniciar sesión con credenciales.")
def login(request: LoginRequest):
    if request.usuario == "admin" and request.password == "1234":
        return {"mensaje": "Inicio de sesión exitoso", "access_token": "token_valido"}
    raise HTTPException(status_code=401, detail="Credenciales inválidas")