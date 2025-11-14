from pydantic import BaseModel

class ProgressOut(BaseModel):
    id: int
    user_uid: str
    routine_id: int

    class Config:
        from_attributes = True  # ✅ reemplaza orm_mode en Pydantic v2
