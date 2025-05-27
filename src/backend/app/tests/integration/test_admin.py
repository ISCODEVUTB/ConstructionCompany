from fastapi.testclient import TestClient
from src.backend.app.api.main import app

client = TestClient(app)

def test_usuario_sin_permiso_no_accede():
    # Simula un token inválido (no autorizado o sin permisos)
    headers = {"Authorization": "Bearer token_invalido"}
    response = client.get("/admin/zona-restringida", headers=headers)

    # Espera 403 Forbidden (token válido pero sin permisos) o 401 Unauthorized (token inválido o expirado)
    assert response.status_code in [401, 403]
