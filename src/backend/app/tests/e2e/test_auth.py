from fastapi.testclient import TestClient
from backend.app.api.main import app

client = TestClient(app)

def test_obtener_token():
    login_data = {"username": "admin", "password": "1234"}
    response = client.post("/auth/token", data=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()