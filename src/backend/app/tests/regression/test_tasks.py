import pytest
from fastapi.testclient import TestClient
from src.backend.app.api.main import app

client = TestClient(app)

@pytest.fixture
def tarea_data():
    return {
        "titulo": "Tarea de prueba",
        "descripcion": "Descripción de la tarea",
        "estado": "pendiente",
        "id": None
    }

def test_listar_tareas_vacio():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert response.json() == []

def test_crear_tarea(tarea_data):
    response = client.post("/tasks/", json=tarea_data)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data and data["id"]
    assert data["titulo"] == tarea_data["titulo"]

def test_actualizar_tarea(tarea_data):
    # Crear tarea
    response = client.post("/tasks/", json=tarea_data)
    tarea = response.json()
    tarea_id = tarea["id"]
    # Actualizar tarea
    tarea_actualizada = tarea.copy()
    tarea_actualizada["titulo"] = "Tarea actualizada"
    response = client.put(f"/tasks/{tarea_id}", json=tarea_actualizada)
    assert response.status_code == 200
    assert response.json()["titulo"] == "Tarea actualizada"

def test_actualizar_tarea_inexistente(tarea_data):
    response = client.put("/tasks/invalid-id", json=tarea_data)
    assert response.status_code == 404

def test_eliminar_tarea():
    # Crear tarea
    tarea_data = {
        "titulo": "Eliminar",
        "descripcion": "Eliminar",
        "estado": "pendiente",
        "id": None
    }
    response = client.post("/tasks/", json=tarea_data)
    tarea_id = response.json()["id"]
    # Eliminar tarea
    response = client.delete(f"/tasks/{tarea_id}")
    assert response.status_code == 204

def test_eliminar_tarea_inexistente():
    response = client.delete("/tasks/invalid-id")
    assert response.status_code == 404