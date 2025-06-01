import pytest
from fastapi.testclient import TestClient
from src.backend.app.api.main import app

client = TestClient(app)

@pytest.fixture
def usuario_data():
    return {
        "nombre": "Usuario Prueba",
        "email": "usuario@prueba.com",
        "rol": "admin",
        "id": None
    }

def test_listar_usuarios_vacio():
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == []

def test_crear_usuario(usuario_data):
    response = client.post("/users/", json=usuario_data)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data and data["id"]
    assert data["nombre"] == usuario_data["nombre"]
    assert data["email"] == usuario_data["email"]
    assert data["rol"] == usuario_data["rol"]

def test_eliminar_usuario():
    usuario = {
        "nombre": "Eliminar",
        "email": "eliminar@prueba.com",
        "rol": "user",
        "id": None
    }
    response = client.post("/users/", json=usuario)
    usuario_id = response.json()["id"]
    response = client.delete(f"/users/{usuario_id}")
    assert response.status_code == 204

def test_eliminar_usuario_inexistente():
    response = client.delete("/users/invalid-id")
    assert response.status_code == 404