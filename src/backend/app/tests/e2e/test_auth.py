from fastapi.testclient import TestClient
from src.backend.app.api.main import app
from src.backend.app.api.models.auth import LoginRequest, Token
from src.backend.app.api.endpoints.auth import get_current_user
from fastapi import HTTPException
import pytest

def test_login_request_model():
    data = {"usuario": "admin", "password": "1234"}
    login = LoginRequest(**data)
    assert login.usuario == "admin"
    assert login.password == "1234"

def test_token_model():
    token = Token(access_token="abc123", token_type="bearer")
    assert token.access_token == "abc123"
    assert token.token_type == "bearer"

def test_get_current_user_valido():
    user = get_current_user(token="token_valido")
    assert user == {"username": "admin"}

def test_get_current_user_invalido():
    with pytest.raises(HTTPException) as excinfo:
        get_current_user(token="token_invalido")
    assert excinfo.value.status_code == 401
    assert "Token inválido" in excinfo.value.detail

client = TestClient(app)

def test_obtener_token():
    login_data = {"username": "admin", "password": "1234"}
    response = client.post("/auth/token", data=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()