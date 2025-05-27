from fastapi.testclient import TestClient
from backend.app.api.main import app

client = TestClient(app)

def obtener_token():
    login_data = {"username": "admin", "password": "1234"}
    response = client.post("/auth/token", data=login_data)
    assert response.status_code == 200
    return response.json()["access_token"]

def test_crear_cliente():
    token = obtener_token()
    headers = {"Authorization": f"Bearer {token}"}
    cliente = {"nombre": "Constructora S.A.", "documento": "1234567890"}
    response = client.post("/clientes/", json=cliente, headers=headers)
    assert response.status_code == 201
    assert "id" in response.json()