from fastapi.testclient import TestClient
from backend.app.api.main import app

client = TestClient(app)

def obtener_token():
    login_data = {"username": "admin", "password": "1234"}
    response = client.post("/auth/token", data=login_data)
    assert response.status_code == 200
    return response.json()["access_token"]

def test_crear_cotizacion():
    token = obtener_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    # Primero crea un cliente
    cliente = {"nombre": "Constructora S.A.", "documento": "1234567890"}
    response = client.post("/clientes/", json=cliente, headers=headers)
    assert response.status_code == 201
    cliente_id = response.json()["id"]

    # Ahora crea la cotización
    cotizacion = {"cliente_id": str(cliente_id), "total": 5000}
    response = client.post("/cotizaciones/", json=cotizacion, headers=headers)
    assert response.status_code == 201
    data = response.json()
    assert str(data["cliente_id"]) == str(cliente_id)
    assert data["total"] == 5000