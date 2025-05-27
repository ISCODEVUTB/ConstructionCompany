from fastapi.testclient import TestClient
from backend.app.api.main import app

client = TestClient(app)


def test_crud_equipo():
    headers = {"Authorization": "Bearer token_valido"}
    equipo = {"nombre": "Retroexcavadora", "estado": "disponible", "ubicacion": "Zona Sur"}

    r = client.post("/equipos/", json=equipo, headers=headers)
    assert r.status_code == 201

    id_equipo = r.json()["id"]
    r = client.get(f"/equipos/{id_equipo}", headers=headers)
    assert r.status_code == 200

    r = client.delete(f"/equipos/{id_equipo}", headers=headers)
    assert r.status_code == 204

def test_acceso_restringido_sin_token():
    response = client.get("/equipos/")
    assert response.status_code == 401
    assert (
        "Token inválido" in response.text
        or "Token inválido o expirado" in response.text
        or "Not authenticated" in response.text
    )
    assert response.headers["WWW-Authenticate"] == "Bearer"

def test_acceso_con_token_invalido():
    response = client.get(
        "/equipos/",
        headers={"Authorization": "Bearer token_invalido"}
    )
    assert response.status_code == 401
    assert (
        "Token inválido" in response.text
        or "Token inválido o expirado" in response.text
        or "Not authenticated" in response.text
    )

def test_acceso_con_token_valido():
    login_response = client.post(
        "/auth/token",
        data={"username": "admin", "password": "1234"}
    )
    token = login_response.json()["access_token"]
    response = client.get(
        "/equipos/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200