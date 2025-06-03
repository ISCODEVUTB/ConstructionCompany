from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.backend.app.api.models.auth import Token
from typing import Optional

router = APIRouter(tags=["autenticacion"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    if not form_data.username or not form_data.password:
        raise HTTPException(
            status_code=400,
            detail="Usuario y contraseña requeridos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if form_data.username == "admin" and form_data.password == "1234":
        return {
            "access_token": "token_valido",
            "token_type": "bearer"
        }
    raise HTTPException(
        status_code=401,
        detail="Credenciales incorrectas",
        headers={"WWW-Authenticate": "Bearer"},
    )

def get_current_user(token: str = Depends(oauth2_scheme)):
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Token requerido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if token != "token_valido":
        raise HTTPException(
            status_code=401,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"username": "admin"}