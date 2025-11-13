from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ------------------- BASE DE DATOS -------------------
from app.db.session import engine
from app.db.base import Base

# ------------------- ROUTERS -------------------
from app.routers.dashboard import router as dashboard_router
from app.routers.routines import router as routines_router
from app.routers.oracle import router as oracle_router
# aquí puedes agregar más routers en el futuro (ej: auth, admin, etc.)

# ------------------- CONFIGURACIÓN DE LA APP -------------------
app = FastAPI(
    title="VideojuegoApp Backend",
    description="API para gestionar usuarios, rutinas y progreso del videojuego",
    version="1.0.0"
)

# ------------------- CORS -------------------
origins = [
    "http://localhost:3000",   # frontend local
    "http://127.0.0.1:3000",   # otra forma de acceder al frontend
    "*"                        # abierto a todos (puedes restringir más adelante)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------- EVENTOS -------------------
@app.on_event("startup")
def on_startup():
    """Crear tablas automáticamente al iniciar la aplicación."""
    Base.metadata.create_all(bind=engine)

# ------------------- REGISTRO DE ROUTERS -------------------
app.include_router(dashboard_router)
app.include_router(routines_router)
app.include_router(oracle_router)