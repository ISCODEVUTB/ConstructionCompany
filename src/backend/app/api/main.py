from fastapi import FastAPI
from backend.app.api.endpoints import auth, dashboard, admin
from src.backend.app.api.endpoints import clients, inventory, projects, quotes, teams

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
app.include_router(teams.router, prefix="/equipos", tags=["Equipos"])
app.include_router(projects.router, prefix="/proyectos", tags=["Proyectos"])
app.include_router(quotes.router, prefix="/cotizaciones", tags=["Cotizaciones"])
app.include_router(auth.router, prefix="/auth", tags=["Autenticación"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(clients.router, prefix="/clientes", tags=["Clientes"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(inventory.router, prefix="/inventarios", tags=["Inventarios"])
