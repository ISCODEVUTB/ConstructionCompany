from fastapi.testclient import TestClient
from src.backend.app.api.main import app

client = TestClient(app)

def test_create_purchase():
    data = {
        "item_name": "Cemento",
        "quantity": 100,
        "price": 250.5,
        "supplier": "Proveedor XYZ"
    }
    response = client.post("/purchases/", json=data)
    assert response.status_code == 201
    result = response.json()
    assert result["item_name"] == data["item_name"]
    assert result["quantity"] == data["quantity"]
    assert result["price"] == data["price"]
    assert result["supplier"] == data["supplier"]
    assert "id" in result
    assert "purchase_date" in result