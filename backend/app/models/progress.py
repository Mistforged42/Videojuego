from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base  # ✅ usa el Base centralizado

class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)

    # Clave foránea hacia users.uid (String)
    user_uid = Column(String, ForeignKey("users.uid"), nullable=False, index=True)

    # Clave foránea hacia routines.id (Integer)
    routine_id = Column(Integer, ForeignKey("routines.id"), nullable=False, index=True)

    # Relaciones opcionales (actívalas si las necesitas)
    # user = relationship("User", backref="progress_entries")
    # routine = relationship("Routine", backref="progress_entries")
