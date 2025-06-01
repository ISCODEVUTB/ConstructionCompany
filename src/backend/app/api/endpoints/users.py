from fastapi import APIRouter, HTTPException
from typing import List
from uuid import uuid4
from src.backend.app.api.models.users import Usuario

router = APIRouter(tags=["usuarios"])

usuarios_db: List[Usuario] = []

@router.post("/", response_model=Usuario, status_code=201)
def crear_usuario(usuario: Usuario):
    usuario.id = str(uuid4())
    usuarios_db.append(usuario)
    return usuario

@router.get("/", response_model=List[Usuario])
def listar_usuarios():
    return usuarios_db

@router.delete("/{usuario_id}", status_code=204)
def eliminar_usuario(usuario_id: str):
    for i, usuario in enumerate(usuarios_db):
        if usuario.id == usuario_id:
            usuarios_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Usuario no encontrado")