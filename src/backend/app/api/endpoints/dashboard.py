from fastapi import APIRouter, HTTPException, Header

router = APIRouter()

def verificar_token(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token inválido")
    token = authorization.split(" ")[1]
    if token != "token_valido":
        raise HTTPException(status_code=401, detail="Token inválido")

@router.get("/", summary="Dashboard", description="Vista general del sistema, protegida por token de acceso.")
def dashboard(authorization: str = Header(None)):
    verificar_token(authorization)
    return {"mensaje": "Bienvenido al dashboard"}