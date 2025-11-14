from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base  # ✅ usa el Base centralizado

DATABASE_URL = "sqlite:///./data.db"  # crea data.db en la raíz del proyecto

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # necesario para SQLite en hilos
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para inyectar la sesión en los routers
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 👇 Importa todos tus modelos aquí para que se registren en Base.metadata
from app.models.user import User
from app.models.progress import Progress
from app.models.routine import Routine

# 👇 Crear las tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)
