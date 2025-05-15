from fastapi.testclient import TestClient
from app.main import app  # Asegúrate de que `main.py` tenga una instancia llamada `app`

client = TestClient(app)


def test_crud_equipo():
    equipo = {"nombre": "Retroexcavadora", "estado": "disponible", "ubicacion": "Zona Sur"}

    r = client.post("/registro-equipos/equipos", json=equipo)
    assert r.status_code == 201

    id_equipo = r.json()["id"]
    r = client.get(f"/registro-equipos/equipos/{id_equipo}")
    assert r.status_code == 200

    r = client.delete(f"/registro-equipos/equipos/{id_equipo}")
    assert r.status_code == 204
