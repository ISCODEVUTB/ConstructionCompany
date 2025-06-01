import pytest
from fastapi.testclient import TestClient
from src.backend.app.api.main import app
from src.backend.app.api.models.payments import Pago

# tests/test_payments.py


client = TestClient(app)

def test_listar_pagos_vacio():
    response = client.get("/payments/")
    assert response.status_code == 200
    assert response.json() == []

def test_registrar_pago():
    pago_data = {
        "monto": 1500.0,
        "fecha": "2024-06-01",
        "metodo": "tarjeta",
        "descripcion": "Pago de prueba",
        "id": None
    }
    response = client.post("/payments/", json=pago_data)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data and data["id"]
    assert data["monto"] == pago_data["monto"]
    assert data["fecha"] == pago_data["fecha"]
    assert data["metodo"] == pago_data["metodo"]
    assert data["descripcion"] == pago_data["descripcion"]

def test_listar_pagos_no_vacio():
    pago_data = {
        "monto": 2000.0,
        "fecha": "2024-06-02",
        "metodo": "efectivo",
        "descripcion": "Segundo pago",
        "id": None
    }
    client.post("/payments/", json=pago_data)
    response = client.get("/payments/")
    assert response.status_code == 200
    pagos = response.json()
    assert isinstance(pagos, list)
    assert any(p["descripcion"] == "Segundo pago" for p in pagos)