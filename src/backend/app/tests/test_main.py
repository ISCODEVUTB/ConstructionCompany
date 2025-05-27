from fastapi.testclient import TestClient
from src.backend.app.api.main import app
import uuid

client = TestClient(app)

# ---------------------
# Configuración común
# ---------------------

def obtener_token():
    """Obtiene un token válido para las pruebas"""
    login_data = {"username": "admin", "password": "1234"}
    try:
        # Cambia data= por json= si tu endpoint espera JSON
        response = client.post("/auth/token", data=login_data)
        
        # Debug: Imprime la respuesta si falla
        if response.status_code != 200:
            print(f"Error en autenticación. Status: {response.status_code}, Respuesta: {response.text}")
            return "Bearer token_simulado"  # Token temporal para continuar pruebas
        
        return f"Bearer {response.json()['access_token']}"
    except Exception as e:
        print(f"Error al obtener token: {str(e)}")
        return "Bearer token_simulado"  # Token temporal para continuar pruebas

headers = {"Authorization": obtener_token()}

# ---------------------
# PRUEBAS PARA EQUIPO
# ---------------------

def test_crear_equipo():
    equipo_data = {
        "nombre": "Excavadora",
        "estado": "activo",
        "ubicacion": "Zona A"
    }
    response = client.post("/equipos/", json=equipo_data, headers=headers)
    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == equipo_data["nombre"]
    assert data["estado"] == equipo_data["estado"]
    assert data["ubicacion"] == equipo_data["ubicacion"]
    assert "id" in data
    # Validar que el ID es un UUID válido
    try:
        uuid.UUID(data["id"])
    except ValueError:
        assert False, "ID no es un UUID válido"

def test_listar_equipos():
    response = client.get("/equipos/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    # Verificar que al menos contiene el equipo creado en el test anterior
    assert any(e["nombre"] == "Excavadora" for e in data)

def test_obtener_equipo():
    # Crear un equipo primero
    equipo_data = {
        "nombre": "Bulldozer",
        "estado": "inactivo",
        "ubicacion": "Zona B"
    }
    create_response = client.post("/equipos/", json=equipo_data, headers=headers)
    equipo_id = create_response.json()["id"]

    # Obtener el equipo por ID
    response = client.get(f"/equipos/{equipo_id}", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == equipo_id
    assert data["nombre"] == equipo_data["nombre"]
    assert data["estado"] == equipo_data["estado"]
    assert data["ubicacion"] == equipo_data["ubicacion"]

def test_actualizar_equipo():
    # Crear un equipo primero
    equipo_data = {
        "nombre": "Grua",
        "estado": "activo",
        "ubicacion": "Zona C"
    }
    create_response = client.post("/equipos/", json=equipo_data, headers=headers)
    equipo_id = create_response.json()["id"]

    # Datos actualizados
    updated_data = {
        "nombre": "Grua Actualizada",
        "estado": "inactivo",
        "ubicacion": "Zona D"
    }
    
    # Actualizar el equipo
    response = client.put(
        f"/equipos/{equipo_id}",
        json=updated_data,
        headers=headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == updated_data["nombre"]
    assert data["estado"] == updated_data["estado"]
    assert data["ubicacion"] == updated_data["ubicacion"]

def test_eliminar_equipo():
    # Crear un equipo primero
    equipo_data = {
        "nombre": "Camion",
        "estado": "activo",
        "ubicacion": "Zona E"
    }
    create_response = client.post("/equipos/", json=equipo_data, headers=headers)
    equipo_id = create_response.json()["id"]

    # Eliminar el equipo
    response = client.delete(f"/equipos/{equipo_id}", headers=headers)
    assert response.status_code == 204

    # Verificar que el equipo ya no existe
    response = client.get(f"/equipos/{equipo_id}", headers=headers)
    assert response.status_code == 404

# ---------------------
# PRUEBAS PARA PROYECTO
# ---------------------

def test_crear_proyecto():
    proyecto_data = {
        "nombre": "Construcción de Puente",
        "descripcion": "Proyecto para construir un puente",
        "estado": "en progreso",
        "fecha_inicio": "2023-01-01"
    }
    response = client.post("/proyectos/", json=proyecto_data, headers=headers)
    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == proyecto_data["nombre"]
    assert data["descripcion"] == proyecto_data["descripcion"]
    assert data["estado"] == proyecto_data["estado"]
    assert data["fecha_inicio"] == proyecto_data["fecha_inicio"]
    assert "id" in data

def test_listar_proyectos():
    response = client.get("/proyectos/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    # Verificar que al menos contiene el proyecto creado en el test anterior
    assert any(p["nombre"] == "Construcción de Puente" for p in data)

def test_obtener_proyecto():
    # Crear un proyecto primero
    proyecto_data = {
        "nombre": "Edificio Comercial",
        "descripcion": "Construcción de un edificio comercial",
        "estado": "planeado",
        "fecha_inicio": "2023-02-01"
    }
    create_response = client.post("/proyectos/", json=proyecto_data, headers=headers)
    proyecto_id = create_response.json()["id"]

    # Obtener el proyecto por ID
    response = client.get(f"/proyectos/{proyecto_id}", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == proyecto_id
    assert data["nombre"] == proyecto_data["nombre"]
    assert data["descripcion"] == proyecto_data["descripcion"]
    assert data["estado"] == proyecto_data["estado"]
    assert data["fecha_inicio"] == proyecto_data["fecha_inicio"]

def test_actualizar_proyecto():
    # Crear un proyecto primero
    proyecto_data = {
        "nombre": "Carretera",
        "descripcion": "Construcción de una carretera",
        "estado": "en progreso",
        "fecha_inicio": "2023-03-01"
    }
    create_response = client.post("/proyectos/", json=proyecto_data, headers=headers)
    proyecto_id = create_response.json()["id"]

    # Datos actualizados
    updated_data = {
        "nombre": "Carretera Actualizada",
        "descripcion": "Construcción de una carretera ampliada",
        "estado": "completado",
        "fecha_inicio": "2023-03-01",
        "fecha_fin": "2023-06-01"
    }
    
    # Actualizar el proyecto
    response = client.put(
        f"/proyectos/{proyecto_id}",
        json=updated_data,
        headers=headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == updated_data["nombre"]
    assert data["descripcion"] == updated_data["descripcion"]
    assert data["estado"] == updated_data["estado"]
    assert data["fecha_fin"] == updated_data["fecha_fin"]

def test_eliminar_proyecto():
    # Crear un proyecto primero
    proyecto_data = {
        "nombre": "Hospital",
        "descripcion": "Construcción de un hospital",
        "estado": "planeado",
        "fecha_inicio": "2023-04-01"
    }
    create_response = client.post("/proyectos/", json=proyecto_data, headers=headers)
    proyecto_id = create_response.json()["id"]

    # Eliminar el proyecto
    response = client.delete(f"/proyectos/{proyecto_id}", headers=headers)
    assert response.status_code == 204

    # Verificar que el proyecto ya no existe
    response = client.get(f"/proyectos/{proyecto_id}", headers=headers)
    assert response.status_code == 404