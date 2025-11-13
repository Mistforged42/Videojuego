from sqlalchemy import Column, Integer, String
from app.db.base import Base  # ✅ usa el Base centralizado

class Routine(Base):
    __tablename__ = "routines"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    duration = Column(String, nullable=False)
