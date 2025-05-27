from fastapi.testclient import TestClient
from src.backend.app.api.main import app

client = TestClient(app)

def test_zona_restringida_sin_token():
    response = client.get("/admin/zona-restringida")
    assert response.status_code == 403

def test_zona_restringida_token_invalido():
    response = client.get(
        "/admin/zona-restringida",
        headers={"Authorization": "Bearer token_invalido"}
    )
    assert response.status_code == 403

def test_zona_restringida_token_valido():
    response = client.get(
        "/admin/zona-restringida",
        headers={"Authorization": "Bearer token_valido"}
    )
    assert response.status_code == 200
    assert response.json() == {"mensaje": "Acceso concedido a la zona restringida"}
