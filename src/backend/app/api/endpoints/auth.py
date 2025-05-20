from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Optional
import secrets

router = APIRouter()

# Configuración de seguridad
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class LoginRequest(BaseModel):
    usuario: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Datos de usuarios (deberían estar en DB en producción)
USUARIOS = {
    "admin": {
        "password": "1234",
        "habilitado": True
    }
}

def verificar_token(token: str = Depends(oauth2_scheme)):
    if token != "token_valido":
        raise HTTPException(
            status_code=401,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"}
        )

@router.post("/token", response_model=Token)
def login(request: LoginRequest):
    user = USUARIOS.get(request.usuario)
    if not user or user["password"] != request.password or not user["habilitado"]:
        raise HTTPException(
            status_code=401,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    return {"access_token": "token_valido", "token_type": "bearer"}