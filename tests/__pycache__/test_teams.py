from fastapi.testclient import TestClient
from frontend.src.main import app

client = TestClient(app)

def test_create_team():
    response = client.post("/teams", json={
        "id": 1,
        "name": "Team A",
        "members_count": 5,
        "project_id": 1
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Team A"

def test_get_teams():
    response = client.get("/teams")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_team():
    response = client.get("/teams/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_update_team():
    response = client.put("/teams/1", json={
        "id": 1,
        "name": "Team B",
        "members_count": 6,
        "project_id": 1
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Team B"

def test_delete_team():
    response = client.delete("/teams/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Team deleted"
