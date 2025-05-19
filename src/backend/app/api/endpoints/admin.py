from fastapi import APIRouter, HTTPException, Header

router = APIRouter()

@router.get("/zona-restringida", summary="Zona restringida", description="Endpoint protegido solo accesible con autorización válida.")
def zona_restringida(authorization: str = Header(None)):
    if authorization != "***":
        raise HTTPException(status_code=403, detail="Acceso denegado")
    return {"mensaje": "Acceso concedido a la zona restringida"}