from pydantic import BaseModel
from typing import List

class RoutineOut(BaseModel):
    id: int
    title: str
    duration: str

    class Config:
        orm_mode = True

class UserOut(BaseModel):
    name: str
    level: int
    xp: int
    xp_needed: int

    class Config:
        orm_mode = True

class DashboardOut(BaseModel):
    user: UserOut
    completed_routines: List[RoutineOut]
    available_routines: List[RoutineOut]

    class Config:
        orm_mode = True