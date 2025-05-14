from fastapi.testclient import TestClient
from app.main import app  # Asegúrate de que `main.py` tenga una instancia llamada `app`

client = TestClient(app)


def test_login_y_dashboard():
    login_data = {"usuario": "admin", "password": "1234"}
    response = client.post("/login", data=login_data)
    assert response.status_code == 200

    token = response.json().get("access_token")
    dashboard = client.get("/dashboard", headers={"Authorization": f"Bearer {token}"})
    assert dashboard.status_code == 200
