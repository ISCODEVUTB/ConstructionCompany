from http import client
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4

app = FastAPI(
    title="API de Construcción",
    description="Documentación de la API para la gestión de proyectos y equipos.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_version="3.1.0"  # Usamos OpenAPI 3.1.0 por compatibilidad con Pydantic v2
)

@app.get("/", summary="Página de bienvenida", description="Devuelve un mensaje de bienvenida.")
def read_root():
    return {"mensaje": "Bienvenido a la API"}

# ---------------------
# MODELOS SIMPLES
# ---------------------

class Equipo(BaseModel):
    id: Optional[str] = Field(None, description="ID único del equipo")
    nombre: str = Field(..., description="Nombre del equipo")
    estado: str = Field(..., description="Estado actual del equipo (activo/inactivo)")
    ubicacion: str = Field(..., description="Ubicación del equipo")
    materiales: List[str] = Field(default_factory=list, description="Lista de materiales asociados al equipo")
    proyectos: List[str] = Field(default_factory=list, description="Lista de IDs de proyectos asociados al equipo")
    fecha_asignacion: Optional[str] = Field(None, description="Fecha de asignación del equipo a un proyecto")
    fecha_desasignacion: Optional[str] = Field(None, description="Fecha de desasignación del equipo de un proyecto")

class Proyecto(BaseModel):
    id: Optional[str] = Field(None, description="ID único del proyecto")
    nombre: str = Field(..., description="Nombre del proyecto")
    descripcion: str = Field(..., description="Descripción del proyecto")
    estado: str = Field(..., description="Estado actual del proyecto")
    fecha_inicio: str = Field(..., description="Fecha de inicio del proyecto")
    fecha_fin: Optional[str] = Field(None, description="Fecha de finalización del proyecto")
    materiales: List[str] = Field(default_factory=list, description="Lista de materiales asociados al proyecto")
    equipos: List[Equipo] = Field(default_factory=list, description="Lista de equipos asignados al proyecto")

class LoginRequest(BaseModel):
    usuario: str
    password: str

class Cotizacion(BaseModel):
    id: Optional[str] = Field(None, description="ID único de la cotización")
    cliente_id: str = Field(..., description="ID del cliente asociado a la cotización")
    total: float = Field(..., description="Monto total de la cotización")

# ---------------------
# BASES DE DATOS EN MEMORIA
# ---------------------
equipos_db: List[Equipo] = []
proyectos_db: List[Proyecto] = []
cotizaciones_db: List[Cotizacion] = []

# ---------------------
# ENDPOINTS CRUD
# ---------------------

EQUIPO_NO_ENCONTRADO = "Equipo no encontrado"

@app.post("/registro-equipos/equipos", status_code=201, summary="Crear equipo", description="Crea un nuevo equipo y lo agrega a la base de datos.")
def crear_equipo(equipo: Equipo):
    equipo.id = str(uuid4())
    equipos_db.append(equipo)
    return equipo

@app.get("/registro-equipos/equipos", response_model=List[Equipo], summary="Listar equipos", description="Devuelve una lista de todos los equipos registrados.")
def listar_equipos(authorization: str = Header(None)):
    if authorization != "Bearer token_valido":
        raise HTTPException(status_code=401, detail="No autorizado")
    return equipos_db

@app.get("/registro-equipos/equipos/{equipo_id}", response_model=Equipo, summary="Obtener equipo", description="Obtiene un equipo por su ID.")
def obtener_equipo(equipo_id: str):
    for eq in equipos_db:
        if eq.id == equipo_id:
            return eq
    raise HTTPException(status_code=404, detail=EQUIPO_NO_ENCONTRADO)

@app.put("/registro-equipos/equipos/{equipo_id}", response_model=Equipo, summary="Actualizar equipo", description="Actualiza los datos de un equipo existente.")
def actualizar_equipo(equipo_id: str, datos: Equipo):
    for i, eq in enumerate(equipos_db):
        if eq.id == equipo_id:
            equipos_db[i] = datos.model_copy(update={"id": equipo_id})
            return equipos_db[i]
    raise HTTPException(status_code=404, detail=EQUIPO_NO_ENCONTRADO)

@app.delete("/registro-equipos/equipos/{equipo_id}", status_code=204, summary="Eliminar equipo", description="Elimina un equipo por su ID.")
def eliminar_equipo(equipo_id: str):
    for i, eq in enumerate(equipos_db):
        if eq.id == equipo_id:
            equipos_db.pop(i)
            return
    raise HTTPException(status_code=404, detail=EQUIPO_NO_ENCONTRADO)

@app.post("/proyectos", status_code=201, response_model=Proyecto, summary="Crear proyecto", description="Crea un nuevo proyecto y lo agrega a la base de datos.")
def crear_proyecto(proyecto: Proyecto):
    proyecto.id = str(uuid4())
    proyectos_db.append(proyecto)
    return proyecto

@app.get("/proyectos", response_model=List[Proyecto], summary="Listar proyectos", description="Devuelve una lista de todos los proyectos registrados.")
def listar_proyectos():
    return proyectos_db

@app.get("/proyectos/{proyecto_id}", response_model=Proyecto, summary="Obtener proyecto", description="Obtiene un proyecto por su ID.")
def obtener_proyecto(proyecto_id: str):
    for proyecto in proyectos_db:
        if proyecto.id == proyecto_id:
            return proyecto
    raise HTTPException(status_code=404, detail="Proyecto no encontrado")

@app.put("/proyectos/{proyecto_id}", response_model=Proyecto, summary="Actualizar proyecto", description="Actualiza los datos de un proyecto existente.")
def actualizar_proyecto(proyecto_id: str, datos: Proyecto):
    for i, proyecto in enumerate(proyectos_db):
        if proyecto.id == proyecto_id:
            proyectos_db[i] = datos.model_copy(update={"id": proyecto_id})
            return proyectos_db[i]
    raise HTTPException(status_code=404, detail="Proyecto no encontrado")

@app.delete("/proyectos/{proyecto_id}", status_code=204, summary="Eliminar proyecto", description="Elimina un proyecto por su ID.")
def eliminar_proyecto(proyecto_id: str):
    for i, proyecto in enumerate(proyectos_db):
        if proyecto.id == proyecto_id:
            proyectos_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Proyecto no encontrado")

@app.post("/login", summary="Iniciar sesión", description="Permite a un usuario iniciar sesión con credenciales.")
def login(request: LoginRequest):
    if request.usuario == "admin" and request.password == "1234":
        return {"mensaje": "Inicio de sesión exitoso", "access_token": "token_valido"}
    raise HTTPException(status_code=401, detail="Credenciales inválidas")

@app.post("/clientes/", status_code=201, summary="Crear cliente", description="Crea un nuevo cliente con datos libres.")
def crear_cliente(cliente: dict):
    cliente["id"] = str(uuid4())
    return cliente

@app.post("/inventarios/registro", summary="Registrar inventario", description="Registra un nuevo inventario, validando si hay materiales repetidos.")
def registrar_inventario(data: dict):
    materiales_repetidos = [m for m in data["materiales"] if data["materiales"].count(m) > 1]
    if materiales_repetidos:
        return {"mensaje": "Material repetido detectado", "materiales_repetidos": materiales_repetidos}
    return {"mensaje": "Registro exitoso"}

@app.post("/cotizaciones/", status_code=201, summary="Crear cotización", description="Crea una nueva cotización con cliente y total.")
def crear_cotizacion(cotizacion: Cotizacion):
    cotizacion.id = str(uuid4())
    cotizaciones_db.append(cotizacion)
    return cotizacion

@app.get("/admin/zona-restringida", summary="Zona restringida", description="Endpoint protegido solo accesible con autorización válida.")
def zona_restringida(authorization: str = Header(None)):
    if authorization != "Bearer token_valido":
        raise HTTPException(status_code=403, detail="Acceso denegado")
    return {"mensaje": "Acceso permitido"}

@app.get("/dashboard", summary="Dashboard", description="Vista general del sistema, protegida por token de acceso.")
def dashboard(authorization: str = Header(None)):
    if authorization != "Bearer token_valido":
        raise HTTPException(status_code=401, detail="No autorizado")
    return {"mensaje": "Bienvenido al dashboard"}
