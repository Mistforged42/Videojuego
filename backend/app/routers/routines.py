from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Dict, List
from app.schemas.routine import RoutineOut
from app.models.routine import Routine
from app.models.user import User
from app.models.progress import Progress
from app.core.deps import get_db

router = APIRouter(prefix="/v1/routines", tags=["routines"])

# ------------------- LISTAR RUTINAS -------------------
@router.get("/")
def get_routines(db: Session = Depends(get_db)) -> Dict[str, List[RoutineOut]]:
    # seed mínimo si la tabla está vacía
    if db.query(Routine).count() == 0:
        seed = [
            Routine(title="Calentamiento rápido 🏃", duration="5 min"),
            Routine(title="Ejercicios de fuerza 💪", duration="15 min"),
            Routine(title="Estiramientos 🧘", duration="10 min"),
        ]
        db.add_all(seed)
        db.commit()

    routines = db.query(Routine).all()
    return {"routines": routines}

# ------------------- COMPLETAR RUTINA -------------------
@router.post("/{routine_id}/complete")
def complete_routine(routine_id: int, user_uid: str, db: Session = Depends(get_db)):
    # buscar usuario por uid
    user = db.query(User).filter(User.uid == user_uid).first()
    if not user:
        return {"error": f"Usuario {user_uid} no encontrado"}


    # verificar rutina
    routine = db.query(Routine).filter(Routine.id == routine_id).first()
    if not routine:
        return {"error": f"Rutina {routine_id} no encontrada"}


    # registrar progreso
    progress = Progress(user_uid=user.uid, routine_id=routine.id)  # ✅ usar user_uid
    db.add(progress)


    # dar XP por rutina
    user.xp += 10
    if user.xp >= user.xp_needed:
        user.level += 1
        user.xp = user.xp - user.xp_needed
        user.xp_needed += 50

    db.commit()
    db.refresh(user)

    return {
        "message": f"{user.name} completó '{routine.title}' y ganó 10 XP",
        "user": {
            "level": user.level,
            "xp": user.xp,
            "xp_needed": user.xp_needed
        }
    }