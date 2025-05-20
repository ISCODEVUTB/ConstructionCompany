from fastapi.testclient import TestClient
from backend.app.api.main import app

client = TestClient(app)

def obtener_token():
    login_data = {"username": "admin", "password": "1234"}
    response = client.post("/auth/token", data=login_data)
    assert response.status_code == 200
    return response.json()["access_token"]

def test_material_repetido_no_rompe_registro():
    token = obtener_token()
    headers = {"Authorization": f"Bearer {token}"}

    data = {
        "materiales": ["cemento", "cemento", "arena"],
        "proyecto_id": 1
    }

    r = client.post("/inventarios/registro", json=data, headers=headers)
    assert r.status_code == 200
    assert "cemento" in r.text
