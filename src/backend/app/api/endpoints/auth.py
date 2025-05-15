from fastapi import APIRouter, HTTPException
from api.models.auth import LoginRequest

router = APIRouter()

@router.post("/login")
def login(request: LoginRequest):
    if request.usuario == "admin" and request.password == "1234":
        return {"mensaje": "Inicio de sesión exitoso", "access_token": "token_valido"}
    raise HTTPException(status_code=401, detail="Credenciales inválidas")