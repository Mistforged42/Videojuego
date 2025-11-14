from pydantic import BaseModel

class RoutineOut(BaseModel):
    id: int
    title: str
    duration: str

    class Config:
        from_attributes = True
