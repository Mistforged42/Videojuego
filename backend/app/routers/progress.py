from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models.progress import Progress
from app.schemas.progress import ProgressOut
from app.core.deps import get_db

router = APIRouter(prefix="/v1/progress", tags=["progress"])

@router.post("/", response_model=ProgressOut)
def create_progress(progress: ProgressOut, db: Session = Depends(get_db)):
    new_progress = Progress(
        user_uid=progress.user_uid,
        routine_id=progress.routine_id
    )
    db.add(new_progress)
    db.commit()
    db.refresh(new_progress)
    return new_progress

@router.get("/{user_uid}", response_model=List[ProgressOut])
def get_progress(user_uid: str, db: Session = Depends(get_db)):
    return db.query(Progress).filter(Progress.user_uid == user_uid).all()
