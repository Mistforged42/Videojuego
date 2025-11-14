from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ------------------- BASE DE DATOS -------------------
from app.db.session import engine  # engine ya crea tablas en session.py

# ------------------- ROUTERS -------------------
from app.routers.dashboard import router as dashboard_router
from app.routers.routines import router as routines_router
from app.routers.oracle import router as oracle_router
from app.routers.profile import router as profile_router
from app.routers.progress import router as progress_router

# ------------------- CONFIGURACIÓN DE LA APP -------------------
app = FastAPI(
    title="VideojuegoApp Backend",
    description="API para gestionar usuarios, rutinas y progreso del videojuego",
    version="1.0.0"
)

# ------------------- CORS -------------------
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------- REGISTRO DE ROUTERS -------------------
app.include_router(dashboard_router)
app.include_router(routines_router)
app.include_router(oracle_router)
app.include_router(profile_router)
app.include_router(progress_router)