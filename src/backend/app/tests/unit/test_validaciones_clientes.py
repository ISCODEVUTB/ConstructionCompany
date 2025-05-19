# Validación simple del RUT o cédula
from fastapi.testclient import TestClient
from backend.app.api.main import app
import re
client = TestClient(app)


def validar_documento(doc):
    return re.match(r"^\d{6,10}$", doc)

def test_validar_documento_valido():
    assert validar_documento("1023456789")

def test_validar_documento_invalido():
    assert not validar_documento("abc123")
