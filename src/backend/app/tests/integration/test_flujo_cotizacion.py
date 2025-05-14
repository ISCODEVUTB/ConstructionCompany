from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_flujo_completo_cotizacion():
    cliente = {"nombre": "Constructora S.A.", "documento": "1234567890"}
    response = client.post("/clientes/", json=cliente)
    assert response.status_code == 201

    cotizacion = {"cliente_id": 1, "total": 5000}
    response = client.post("/cotizaciones/", json=cotizacion)
    assert response.status_code == 201
