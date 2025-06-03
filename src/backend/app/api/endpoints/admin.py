from fastapi import APIRouter, HTTPException, Header

router = APIRouter()

@router.get("/zona-restringida", summary="Zona restringida", description="Endpoint protegido solo accesible con autorización válida.")
def zona_restringida(authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(status_code=403, detail="Falta el header Authorization")
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Formato de Authorization inválido")
    token = authorization[7:]
    if not token:
        raise HTTPException(status_code=403, detail="Token vacío")
    if token != "token_valido":
        raise HTTPException(status_code=403, detail="Acceso denegado")
    return {"mensaje": "Acceso concedido a la zona restringida"}