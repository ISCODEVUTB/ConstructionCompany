import pytest
from backend.models import Equipment, Project

def test_equipment_creation():
    """Prueba la creación básica de un equipo"""
    equipment = Equipment(
        name="Excavadora CAT",
        status="available",
        last_maintenance="2024-01-01"
    )
    assert equipment.name == "Excavadora CAT"
    assert equipment.status == "available"

def test_project_required_fields():
    """Verifica que los campos obligatorios sean validados"""
    with pytest.raises(ValueError):
        Project(name=None)
