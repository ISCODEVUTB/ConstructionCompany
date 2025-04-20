# filepath: /workspaces/ConstructionCompany/frontend/src/main.py
from fastapi import FastAPI
from backend.routers import equipos  # Importa el router de equipos

app = FastAPI()

# Incluir el router de equipos
app.include_router(equipos.router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

