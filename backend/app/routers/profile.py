from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.auth import verify_token
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserSchema

router = APIRouter(prefix="/v1", tags=["profile"])

@router.get("/profile", response_model=UserSchema)
def get_profile(payload: dict = Depends(verify_token), db: Session = Depends(get_db)):
    """Devuelve el perfil del usuario autenticado, creando uno si no existe"""
    uid = payload.get("sub")
    email = payload.get("email", "unknown@example.com")

    # Buscar usuario en la base de datos
    user = db.query(User).filter(User.uid == uid).first()

    # Si no existe, crearlo con valores iniciales
    if not user:
        user = User(
            uid=uid,
            email=email,
            name=None,  # el frontend puede actualizarlo luego
            avatar="default.png",
            level=1,
            xp=0,
            xp_needed=100
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    return user
