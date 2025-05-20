from fastapi.testclient import TestClient
from backend.app.api.main import app

client = TestClient(app)

def test_acceso_restringido_sin_token():
    # No se incluye header Authorization
    response = client.get("/registro-equipos/equipos")

    # Se espera un 401 Unauthorized por falta de token
    assert response.status_code == 401
    assert "Not authenticated" in response.text or "Unauthorized" in response.text
