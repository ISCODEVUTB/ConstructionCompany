import pytest
from fastapi.testclient import TestClient
from frontend.src.main import app  # Corrige la ruta de importación

client = TestClient(app)

def test_example_route():
    response = client.get("/")  # Cambia "/example" por una ruta válida
    assert response.status_code == 200
