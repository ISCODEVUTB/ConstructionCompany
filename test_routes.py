from fastapi.testclient import TestClient
from frontend.src.main import app

client = TestClient(app)

def test_create_project():
    response = client.post("/projects", json={
        "id": 1,
        "name": "Building A",
        "description": "Construction of Building A",
        "start_date": "2025-05-01",
        "end_date": "2025-12-31",
        "budget": 75000.0
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Building A"

def test_get_projects():
    response = client.get("/projects")
    assert response.status_code == 200
    assert len(response.json()) > 0  # Verifica que haya al menos un proyecto

def test_get_project():
    response = client.get("/projects/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_update_project():
    response = client.put("/projects/1", json={
        "id": 1,
        "name": "Building B",
        "description": "Updated description",
        "start_date": "2025-06-01",
        "end_date": "2025-12-31",
        "budget": 80000.0
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Building B"

def test_delete_project():
    response = client.delete("/projects/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Project deleted"
