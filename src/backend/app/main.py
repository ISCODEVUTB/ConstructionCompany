
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI(title="Construction Company API")

# ---------------------
# MODELOS SIMPLES
# ---------------------

class Equipo(BaseModel):
    id: Optional[str] = None
    nombre: str
    estado: str
    ubicacion: str

# En memoria (por simplicidad)
equipos_db: List[Equipo] = []

# ---------------------
# ENDPOINTS CRUD
# ---------------------

EQUIPO_NO_ENCONTRADO = "Equipo no encontrado"

@app.post("/registro-equipos/equipos", status_code=201)
def crear_equipo(equipo: Equipo):
    equipo.id = str(uuid4())
    equipos_db.append(equipo)
    return equipo

@app.get("/registro-equipos/equipos", response_model=List[Equipo])
def listar_equipos():
    return equipos_db

@app.get("/registro-equipos/equipos/{equipo_id}", response_model=Equipo)
def obtener_equipo(equipo_id: str):
    for eq in equipos_db:
        if eq.id == equipo_id:
            return eq
    raise HTTPException(status_code=404, detail=EQUIPO_NO_ENCONTRADO)

@app.put("/registro-equipos/equipos/{equipo_id}", response_model=Equipo)
def actualizar_equipo(equipo_id: str, datos: Equipo):
    for i, eq in enumerate(equipos_db):
        if eq.id == equipo_id:
            equipos_db[i] = datos.copy(update={"id": equipo_id})
            return equipos_db[i]
    raise HTTPException(status_code=404, detail=EQUIPO_NO_ENCONTRADO)

@app.delete("/registro-equipos/equipos/{equipo_id}", status_code=204)
def eliminar_equipo(equipo_id: str):
    for i, eq in enumerate(equipos_db):
        if eq.id == equipo_id:
            equipos_db.pop(i)
            return
    raise HTTPException(status_code=404, detail=EQUIPO_NO_ENCONTRADO)
