from fastapi import APIRouter, HTTPException, Header

router = APIRouter()

@router.get("/", summary="Dashboard", description="Vista general del sistema, protegida por token de acceso.")
def dashboard(authorization: str = Header(None)):
    if authorization != "***":
        raise HTTPException(status_code=401, detail="Token inválido")
    return {"mensaje": "Bienvenido al dashboard"}