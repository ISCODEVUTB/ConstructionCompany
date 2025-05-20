from fastapi.testclient import TestClient
from backend.app.api.main import app

client = TestClient(app)

def test_acceso_restringido_sin_token():
    response = client.get("/equipos")
    assert response.status_code == 401
    assert "Token inválido" in response.text or "Token inválido o expirado" in response.text
    assert response.headers["WWW-Authenticate"] == "Bearer"

def test_acceso_con_token_invalido():
    response = client.get(
        "/equipos",
        headers={"Authorization": "Bearer token_invalido"}
    )
    assert response.status_code == 401
    assert "Token inválido" in response.text or "Token inválido o expirado" in response.text

def test_acceso_con_token_valido():
    login_response = client.post(
        "/auth/token",
        data={"username": "admin", "password": "1234"}
    )
    token = login_response.json()["access_token"]
    response = client.get(
        "/equipos",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200