from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./data.db"  # crea data.db en la raíz

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # necesario para SQLite en hilos
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)