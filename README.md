# 🏗️ Construction Company - Gestión de Proyectos  

[![FastAPI](https://img.shields.io/badge/fastapi-0.100.0-green)](https://fastapi.tiangolo.com/)
[![Pytest](https://img.shields.io/badge/pytest-tested-brightgreen)](https://docs.pytest.org/)
[![Postgres](https://img.shields.io/badge/postgres-db-blue)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/docker-ready-blue)](https://www.docker.com/)
[![GitHub Actions](https://img.shields.io/badge/github-actions-blue)](https://github.com/features/actions)
[![Coverage](https://img.shields.io/badge/coverage-93%25-brightgreen)](https://pytest-cov.readthedocs.io/)

---

**Sistema integral para optimizar la gestión de proyectos, recursos y costos en empresas de construcción.**  

---

##  Características Principales  
**Gestión Centralizada**:  
   - Control de proyectos, equipos, inventarios y personal en una plataforma unificada.  
   - Dashboards en tiempo real con gráficos interactivos.  

🔌 **Integración con APIs**:  
   - Conexión con sistemas ERP, contabilidad y RRHH mediante APIs REST seguras.  

**Automatización**:  
   - Notificaciones automáticas de disponibilidad de recursos.  
   - Generación diaria de reportes (costos, avances, inventario).  

**Plataforma en la Nube**:  
   - Acceso multiplataforma (web, móvil) con sincronización en tiempo real.  

----

##  Comenzar  

###  Prerrequisitos  
- Python 3.10+  
- PostgreSQL 14+ (o SQLite para desarrollo)  
- Docker (opcional para despliegue)  

---

##  Tecnologías Clave  
| Área          | Tecnologías |  
|---------------|------------|  
| Backend       | Python (FastAPI), PostgreSQL |  
| Frontend      | Flutter |  
| DevOps        | Docker, GitHub Actions |  
| APIs          | REST (OAuth 2.0), Swagger |  


---

## 🚀 Instalación y Ejecución

1. Clona el repositorio:
   ```bash
   git clone <repo-url>
   cd ConstructionCompany
   ```

2. Crea y configura tu entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Configura las variables de entorno:
   - Copia `.env.example` a `.env` y edítalo según tu entorno.

4. Ejecuta la aplicación:
   ```bash
   uvicorn src.backend.app.api.main:app --reload
   ```

## 🧪 Pruebas

- Ejecuta todas las pruebas:
   ```bash
   pytest --cov=src/backend/app --cov-report=xml
   ```

## 📁 Estructura del Proyecto

```
src/backend/app/
├── api/
│   ├── main.py
│   ├── endpoints/
│   ├── models/
│   └── database/
├── tests/
│   └── ...
```

## 📚 Ejemplo de Uso de la API

```http
POST /purchases/
{
  "item_name": "Cemento",
  "quantity": 100,
  "price": 250.5,
  "supplier": "Proveedor XYZ"
}
```

##  Licencia  
MIT © 2025 - [Universidad Tecnológica de Bolívar](https://www.unitecnologica.edu.co/)


