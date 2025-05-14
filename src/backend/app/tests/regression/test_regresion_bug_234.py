from fastapi.testclient import TestClient
from app.main import app  # Asegúrate de que `main.py` tenga una instancia llamada `app`

client = TestClient(app)


def test_material_repetido_no_rompe_registro():
    data = {
        "materiales": ["cemento", "cemento", "arena"],
        "proyecto_id": 1
    }
    r = client.post("/inventarios/registro", json=data)
    assert r.status_code == 200
    assert "cemento" in r.text
