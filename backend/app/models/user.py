from sqlalchemy import Column, Integer, String
from app.db.base import Base  # ✅ usa el Base centralizado para evitar ciclos

class User(Base):
    __tablename__ = "users"

    uid = Column(String, primary_key=True, index=True)
    email = Column(String, index=True, nullable=True)
    name = Column(String, index=True, nullable=True)
    level = Column(Integer, default=1, nullable=False)
    xp = Column(Integer, default=0, nullable=False)
    xp_needed = Column(Integer, default=100, nullable=False)
    avatar = Column(String, default="default.png")
