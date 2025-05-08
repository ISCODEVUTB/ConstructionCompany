from fastapi.testclient import TestClient
from frontend.src.main import app

client = TestClient(app)

def test_create_employee():
    response = client.post("/employees", json={
        "id": 1,
        "name": "John Doe",
        "role": "Engineer",
        "team_id": 1
    })
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_get_employees():
    response = client.get("/employees")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_employee():
    response = client.get("/employees/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_update_employee():
    response = client.put("/employees/1", json={
        "id": 1,
        "name": "Jane Doe",
        "role": "Manager",
        "team_id": 1
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"

def test_delete_employee():
    response = client.delete("/employees/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Employee deleted"
