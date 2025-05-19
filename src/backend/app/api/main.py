from fastapi import FastAPI
from backend.app.api.endpoints import equipos, proyectos, cotizaciones, auth, dashboard, clientes, admin, inventarios

app = FastAPI(
    title="API de Construcción",
    description="Documentación de la API para la gestión de proyectos y equipos.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Endpoint raíz
@app.get("/", summary="Página de bienvenida", description="Devuelve un mensaje de bienvenida.")
def read_root():
    return {"mensaje": "Bienvenido a la API de Construcción"}

# Montar los routers con los prefijos que esperan tus tests
app.include_router(equipos.router, prefix="/registro-equipos/equipos", tags=["Equipos"])
app.include_router(proyectos.router, prefix="/proyectos", tags=["Proyectos"])
app.include_router(cotizaciones.router, prefix="/cotizaciones", tags=["Cotizaciones"])
app.include_router(auth.router, prefix="/login", tags=["Autenticación"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(inventarios.router, prefix="/inventarios", tags=["Inventarios"])