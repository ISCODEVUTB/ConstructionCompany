from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)

# ---------------------
# PRUEBAS PARA EQUIPO
# ---------------------

def test_crear_equipo():
    response = client.post("/registro-equipos/equipos", json={
        "nombre": "Excavadora",
        "estado": "activo",
        "ubicacion": "Zona A"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == "Excavadora"
    assert data["estado"] == "activo"
    assert data["ubicacion"] == "Zona A"
    assert "id" in data

def test_listar_equipos():
    response = client.get("/registro-equipos/equipos", headers={"Authorization": "Bearer token_valido"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_obtener_equipo():
    # Crear un equipo primero
    response = client.post("/registro-equipos/equipos", json={
        "nombre": "Bulldozer",
        "estado": "inactivo",
        "ubicacion": "Zona B"
    })
    equipo_id = response.json()["id"]

    # Obtener el equipo por ID
    response = client.get(f"/registro-equipos/equipos/{equipo_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == equipo_id
    assert data["nombre"] == "Bulldozer"

def test_actualizar_equipo():
    # Crear un equipo primero
    response = client.post("/registro-equipos/equipos", json={
        "nombre": "Grua",
        "estado": "activo",
        "ubicacion": "Zona C"
    })
    equipo_id = response.json()["id"]

    # Actualizar el equipo
    response = client.put(f"/registro-equipos/equipos/{equipo_id}", json={
        "nombre": "Grua Actualizada",
        "estado": "inactivo",
        "ubicacion": "Zona D"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Grua Actualizada"
    assert data["estado"] == "inactivo"
    assert data["ubicacion"] == "Zona D"

def test_eliminar_equipo():
    # Crear un equipo primero
    response = client.post("/registro-equipos/equipos", json={
        "nombre": "Camion",
        "estado": "activo",
        "ubicacion": "Zona E"
    })
    equipo_id = response.json()["id"]

    # Eliminar el equipo
    response = client.delete(f"/registro-equipos/equipos/{equipo_id}")
    assert response.status_code == 204

    # Verificar que el equipo ya no existe
    response = client.get(f"/registro-equipos/equipos/{equipo_id}")
    assert response.status_code == 404

# ---------------------
# PRUEBAS PARA PROYECTO
# ---------------------

def test_crear_proyecto():
    response = client.post("/proyectos", json={
        "nombre": "Construcción de Puente",
        "descripcion": "Proyecto para construir un puente",
        "estado": "en progreso",
        "fecha_inicio": "2023-01-01"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == "Construcción de Puente"
    assert data["descripcion"] == "Proyecto para construir un puente"
    assert data["estado"] == "en progreso"
    assert data["fecha_inicio"] == "2023-01-01"
    assert "id" in data

def test_listar_proyectos():
    response = client.get("/proyectos")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_obtener_proyecto():
    # Crear un proyecto primero
    response = client.post("/proyectos", json={
        "nombre": "Edificio Comercial",
        "descripcion": "Construcción de un edificio comercial",
        "estado": "planeado",
        "fecha_inicio": "2023-02-01"
    })
    proyecto_id = response.json()["id"]

    # Obtener el proyecto por ID
    response = client.get(f"/proyectos/{proyecto_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == proyecto_id
    assert data["nombre"] == "Edificio Comercial"

def test_actualizar_proyecto():
    # Crear un proyecto primero
    response = client.post("/proyectos", json={
        "nombre": "Carretera",
        "descripcion": "Construcción de una carretera",
        "estado": "en progreso",
        "fecha_inicio": "2023-03-01"
    })
    proyecto_id = response.json()["id"]

    # Actualizar el proyecto
    response = client.put(f"/proyectos/{proyecto_id}", json={
        "nombre": "Carretera Actualizada",
        "descripcion": "Construcción de una carretera ampliada",
        "estado": "completado",
        "fecha_inicio": "2023-03-01",
        "fecha_fin": "2023-06-01"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Carretera Actualizada"
    assert data["estado"] == "completado"
    assert data["fecha_fin"] == "2023-06-01"

def test_eliminar_proyecto():
    # Crear un proyecto primero
    response = client.post("/proyectos", json={
        "nombre": "Hospital",
        "descripcion": "Construcción de un hospital",
        "estado": "planeado",
        "fecha_inicio": "2023-04-01"
    })
    proyecto_id = response.json()["id"]

    # Eliminar el proyecto
    response = client.delete(f"/proyectos/{proyecto_id}")
    assert response.status_code == 204

    # Verificar que el proyecto ya no existe
    response = client.get(f"/proyectos/{proyecto_id}")
    assert response.status_code == 404