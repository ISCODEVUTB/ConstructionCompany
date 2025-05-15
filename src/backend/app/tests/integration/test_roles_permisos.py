from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)


def test_usuario_sin_permiso_no_accede():
    response = client.get("/admin/zona-restringida", headers={"Authorization": "Bearer token_invalido"})
    assert response.status_code == 403
