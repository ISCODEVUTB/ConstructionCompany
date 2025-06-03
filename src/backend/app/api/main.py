from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API de Construcción",
    description="Documentación de la API para la gestión de proyectos y equipos.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://potential-xylophone-pj7vp975q569c6gx7-3000.app.github.dev",
        "https://potential-xylophone-pj7vp975q569c6gx7-8000.app.github.dev"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Importar rutas DESPUÉS del middleware
from src.backend.app.api.endpoints import auth, dashboard, admin, clients, inventory, projects, quotes, teams, tasks, payments, users, purchase

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
app.include_router(users.router, prefix="/users", tags=["Usuarios"])
app.include_router(payments.router, prefix="/payments", tags=["Pagos"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tareas"])
app.include_router(purchase.router, prefix="/purchase", tags=["Compras"])
