from sqlalchemy.orm import Session
from app.models.user import User
from app.models.progress import Progress
from app.models.routine import Routine

def get_dashboard_data(db: Session, user_name: str):
    # Buscar usuario
    user = db.query(User).filter(User.name == user_name).first()
    if not user:
        user = User(name=user_name, level=2, xp=60, xp_needed=100)
        db.add(user)
        db.commit()
        db.refresh(user)

    # Rutinas completadas
    progress_entries = db.query(Progress).filter(Progress.user_id == user.id).all()
    routine_ids = [p.routine_id for p in progress_entries]
    titles = []
    if routine_ids:
        titles = [r.title for r in db.query(Routine).filter(Routine.id.in_(routine_ids)).all()]

    return {
        "user": user.name,
        "level": user.level,
        "xp": user.xp,
        "xp_needed": user.xp_needed,
        "completed_routines": titles,
    }