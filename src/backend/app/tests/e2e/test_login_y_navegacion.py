from fastapi.testclient import TestClient
from backend.app.api.main import app

client = TestClient(app)

def obtener_token():
    login_data = {"username": "admin", "password": "1234"}
    response = client.post("/auth/token", data=login_data)
    assert response.status_code == 200
    return response.json()["access_token"]

def test_login_y_dashboard():
    token = obtener_token()
    headers = {"Authorization": f"Bearer {token}"}

    dashboard = client.get("/dashboard", headers=headers)
    assert dashboard.status_code == 200
    assert dashboard.json() == {"mensaje": "Bienvenido al dashboard"}

