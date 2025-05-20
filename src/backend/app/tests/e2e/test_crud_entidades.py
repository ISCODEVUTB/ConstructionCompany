from fastapi.testclient import TestClient
from backend.app.api.main import app

client = TestClient(app)


def test_crud_equipo():
    headers = {"Authorization": "Bearer token_valido"}
    equipo = {"nombre": "Retroexcavadora", "estado": "disponible", "ubicacion": "Zona Sur"}

    r = client.post("/registro-equipos/equipos", json=equipo, headers=headers)
    assert r.status_code == 201

    id_equipo = r.json()["id"]
    r = client.get(f"/registro-equipos/equipos/{id_equipo}", headers=headers)
    assert r.status_code == 200

    r = client.delete(f"/registro-equipos/equipos/{id_equipo}", headers=headers)
    assert r.status_code == 204
