from fastapi import FastAPI
from api.endpoints import equipos, proyectos, cotizaciones, auth

app = FastAPI(
    title="API de Construcción",
    description="Documentación de la API para la gestión de proyectos y equipos.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Montar los routers
app.include_router(equipos.router, prefix="/equipos", tags=["Equipos"])
app.include_router(proyectos.router, prefix="/proyectos", tags=["Proyectos"])
app.include_router(cotizaciones.router, prefix="/cotizaciones", tags=["Cotizaciones"])
app.include_router(auth.router, prefix="/auth", tags=["Autenticación"])
