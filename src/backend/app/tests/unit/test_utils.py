from datetime import datetime
from src.backend.app.api.utils.utils import formatear_fecha

def test_formatear_fecha():
    fecha = datetime(2025, 5, 14)
    assert formatear_fecha(fecha) == "14-05-2025"