from fastapi.testclient import TestClient
from frontend.src.main import app

client = TestClient(app)

def test_create_material():
    response = client.post("/materials", json={
        "id": 1,
        "name": "Concrete",
        "quantity": 50,
        "project_id": 1
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Concrete"

def test_get_materials():
    response = client.get("/materials")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_material():
    response = client.get("/materials/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_update_material():
    response = client.put("/materials/1", json={
        "id": 1,
        "name": "Steel",
        "quantity": 100,
        "project_id": 1
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Steel"

def test_delete_material():
    response = client.delete("/materials/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Material deleted"
