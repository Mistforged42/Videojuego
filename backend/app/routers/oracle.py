from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.models.user import User

router = APIRouter(prefix="/v1/oracle", tags=["oracle"])

@router.get("/play")
def play_oracle(db: Session = Depends(get_db), user_name: str = "Ornella"):
    user = db.query(User).filter(User.name == user_name).first()
    if not user:
        user = User(name=user_name, level=1, xp=0, xp_needed=100)
        db.add(user)
        db.commit()
        db.refresh(user)

    user.xp += 20
    if user.xp >= user.xp_needed:
        user.level += 1
        user.xp = user.xp - user.xp_needed
        user.xp_needed += 50
    db.commit()
    db.refresh(user)

    return {"result": f"{user.name} ha ganado 20 XP por completar una rutina 🎉"}