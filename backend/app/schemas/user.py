from pydantic import BaseModel

class UserSchema(BaseModel):
    uid: str
    email: str | None = None
    avatar: str
    xp: int
    level: int

    class Config:
        from_attributes = True  # reemplazo de orm_mode en Pydantic v2
