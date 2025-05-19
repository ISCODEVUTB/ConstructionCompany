from fastapi.testclient import TestClient
from backend.app.api.main import app

client = TestClient(app)


def test_acceso_restringido_sin_token():
    r = client.get("/registro-equipos/equipos")
    assert r.status_code == 401
