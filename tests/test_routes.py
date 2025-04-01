import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_example_route():
    response = client.get("/example")
    assert response.status_code == 200
    assert "key" in response.json()
