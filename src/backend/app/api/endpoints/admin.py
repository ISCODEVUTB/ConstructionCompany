from fastapi import APIRouter, HTTPException, Header

router = APIRouter()

@router.get("/zona-restringida", summary="Zona restringida", description="Endpoint protegido solo accesible con autorización válida.")
def zona_restringida(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Acceso denegado")
    token = authorization.split(" ")[1]
    if token != "token_valido":
        raise HTTPException(status_code=403, detail="Acceso denegado")
    return {"mensaje": "Acceso concedido a la zona restringida"}