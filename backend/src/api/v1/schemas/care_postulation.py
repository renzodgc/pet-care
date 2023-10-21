from typing import Optional
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class CarePostulationCreate(BaseModel):
    name: str
    start_date: datetime
    end_date: datetime
    price_per_day: int
    restrictions: str
    place_traits: str


class CarePostulationOut(CarePostulationCreate):
    caretaker_id: UUID

    class Config:
        orm_mode = True
