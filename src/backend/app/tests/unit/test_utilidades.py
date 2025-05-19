# Función utilitaria para formatear fechas
from fastapi.testclient import TestClient
from backend.app.api.main import app

client = TestClient(app)

from datetime import datetime

def formatear_fecha(fecha):
    return fecha.strftime("%d-%m-%Y")

def test_formatear_fecha():
    fecha = datetime(2025, 5, 14)
    assert formatear_fecha(fecha) == "14-05-2025"