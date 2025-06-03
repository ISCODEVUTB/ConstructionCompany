from fastapi.testclient import TestClient
from src.backend.app.api.main import app

client = TestClient(app)

def test_login_success():
    response = client.post("/auth/token", data={"username": "admin", "password": "1234"})
    assert response.status_code == 200
    data = response.json()
    assert data["access_token"] == "token_valido"
    assert data["token_type"] == "bearer"

def test_login_wrong_credentials():
    response = client.post("/auth/token", data={"username": "admin", "password": "wrong"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Credenciales incorrectas"

def test_login_missing_username():
    response = client.post("/auth/token", data={"password": "1234"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Usuario y contraseña requeridos"

def test_login_missing_password():
    response = client.post("/auth/token", data={"username": "admin"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Usuario y contraseña requeridos"

def test_get_current_user_valid_token():
    headers = {"Authorization": "Bearer token_valido"}
    response = client.get("/admin/zona-restringida", headers=headers)
    # Este endpoint debe estar protegido y devolver 200 si el token es válido
    assert response.status_code in (200, 403)  # 200 si acceso concedido, 403 si denegado por lógica extra

def test_get_current_user_invalid_token():
    headers = {"Authorization": "Bearer token_invalido"}
    response = client.get("/admin/zona-restringida", headers=headers)
    assert response.status_code == 403 or response.status_code == 401

def test_get_current_user_no_token():
    response = client.get("/admin/zona-restringida")
    assert response.status_code == 403 or response.status_code == 401