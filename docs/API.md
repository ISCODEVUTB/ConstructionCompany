# Microservicio de Registro de Equipos

**Proyecto:** System company construction

## 1. Descripción General

Este microservicio tiene como objetivo gestionar el registro de equipos utilizados en los distintos proyectos de construcción de la compañía. Permite listar, registrar, actualizar y eliminar información de maquinaria y equipos.

## 2. Funcionalidades

- `GET /registro-equipos/equipos`  
  Obtiene la lista de equipos registrados.

Opcionales para agregar luego:

- `POST /registro-equipos/equipos` → Registrar un nuevo equipo  
- `PUT /registro-equipos/equipos/{id}` → Actualizar datos de un equipo  
- `DELETE /registro-equipos/equipos/{id}` → Eliminar equipo

## 3. Tecnologías Utilizadas

- Lenguaje: Python  
- Framework: FastAPI  
- Servidor: Uvicorn  
- Estructura Modular: Router, modelos, esquemas

## 4. Estructura del Microservicio

/backend/registro_equipos/
│
├── routes.py
├── models.py
├── schemas.py
└── main.py

Y en `app.py` del backend principal:

```python
from registro_equipos.routes import router as equipos_router
app.include_router(equipos_router, prefix="/registro-equipos")

