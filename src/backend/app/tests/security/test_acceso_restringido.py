from fastapi.testclient import TestClient
from app.main import app  # Asegúrate de que `main.py` tenga una instancia llamada `app`

client = TestClient(app)


def test_acceso_restringido_sin_token():
    r = client.get("/registro-equipos/equipos")
    assert r.status_code == 401
