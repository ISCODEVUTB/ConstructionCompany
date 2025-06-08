from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import uuid4
from src.backend.app.api.models.users import Usuario
from src.backend.app.api.database.schemas.users_db import UsuarioDB
from src.backend.app.api.database.db import SessionLocal
from fastapi.responses import JSONResponse

router = APIRouter(tags=["usuarios"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Usuario, status_code=201)
def crear_usuario(usuario: Usuario, db: Session = Depends(get_db)):
    db_usuario = UsuarioDB(
        id=str(uuid4()),
        nombre=usuario.nombre,
        email=usuario.email,
        password=usuario.password,
        rol=usuario.rol if hasattr(usuario, "rol") else "usuario"  # Valor por defecto si no viene en el request
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@router.get("/", response_model=List[Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(UsuarioDB).all()
    return usuarios

@router.delete("/{usuario_id}", status_code=204)
def eliminar_usuario(usuario_id: str, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).filter(UsuarioDB.id == usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(usuario)
    db.commit()

@router.options("/")
def options_usuarios():
    return JSONResponse(content={"allow": "GET, POST, OPTIONS"}, status_code=200)