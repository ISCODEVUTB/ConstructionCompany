from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Modelo de datos
class Equipo(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str] = None

# Base de datos simulada
equipos_db: List[Equipo] = []

# Crear equipo
@app.post("/equipos/", response_model=Equipo)
def crear_equipo(equipo: Equipo):
    equipos_db.append(equipo)
    return equipo

# Leer todos los equipos
@app.get("/equipos/", response_model=List[Equipo])
def obtener_equipos():
    return equipos_db

# Leer equipo por ID
@app.get("/equipos/{equipo_id}", response_model=Equipo)
def obtener_equipo(equipo_id: int):
    for equipo in equipos_db:
        if equipo.id == equipo_id:
            return equipo
    raise HTTPException(status_code=404, detail="Equipo no encontrado")

# Actualizar equipo
@app.put("/equipos/{equipo_id}", response_model=Equipo)
def actualizar_equipo(equipo_id: int, equipo_actualizado: Equipo):
    for index, equipo in enumerate(equipos_db):
        if equipo.id == equipo_id:
            equipos_db[index] = equipo_actualizado
            return equipo_actualizado
    raise HTTPException(status_code=404, detail="Equipo no encontrado")

# Eliminar equipo
@app.delete("/equipos/{equipo_id}")
def eliminar_equipo(equipo_id: int):
    for index, equipo in enumerate(equipos_db):
        if equipo.id == equipo_id:
            del equipos_db[index]
            return {"mensaje": "Equipo eliminado"}
    raise HTTPException(status_code=404, detail="Equipo no encontrado")

