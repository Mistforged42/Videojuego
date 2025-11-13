from pydantic import BaseModel

class RoutineOut(BaseModel):
    id: int
    title: str
    duration: str

    class Config:
        orm_mode = True