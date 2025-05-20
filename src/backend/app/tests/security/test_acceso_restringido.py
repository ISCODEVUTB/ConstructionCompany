from fastapi.testclient import TestClient
from backend.app.api.main import app

client = TestClient(app)

def test_acceso_restringido_sin_token():
    # No se incluye header Authorization
    response = client.get("/registro-equipos/equipos")
    
    # Verificar código de estado
    assert response.status_code == 401
    # Verificar mensaje de error actualizado
    assert "Token inválido o expirado" in response.text
    # Verificar cabecera WWW-Authenticate
    assert response.headers["WWW-Authenticate"] == "Bearer"

def test_acceso_con_token_invalido():
    response = client.get(
        "/registro-equipos/equipos",
        headers={"Authorization": "Bearer token_invalido"}
    )
    assert response.status_code == 401
    assert "Token inválido o expirado" in response.text

def test_acceso_con_token_valido():
    # Primero obtener token válido
    login_response = client.post(
        "/token",
        data={"username": "admin", "password": "1234"}
    )
    token = login_response.json()["access_token"]
    
    # Luego usarlo para acceder
    response = client.get(
        "/registro-equipos/equipos",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200