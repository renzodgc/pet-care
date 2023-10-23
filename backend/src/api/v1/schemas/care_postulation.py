from typing import Optional
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel
from src.models import Species


class CarePostulationCreate(BaseModel):
    start_date: datetime
    end_date: datetime
    price_per_day: int
    restrictions: str
    place_traits: str
    allowed_species: Species


class CarePostulationRelated(CarePostulationCreate):
    caretaker_id: UUID

    class Config:
        orm_mode = True


class CarePostulationOut(CarePostulationRelated):
    id: UUID

    class Config:
        orm_mode = True
