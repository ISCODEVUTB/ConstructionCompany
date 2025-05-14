from fastapi.testclient import TestClient
from app.main import app  # Asegúrate de que `main.py` tenga una instancia llamada `app`

client = TestClient(app)


def test_usuario_sin_permiso_no_accede():
    response = client.get("/admin/zona-restringida", headers={"Authorization": "Bearer token_invalido"})
    assert response.status_code == 403
