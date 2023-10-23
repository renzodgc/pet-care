from typing import Optional
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class CareRequestCreate(BaseModel):
    start_date: datetime
    end_date: datetime
    request_message: str
    response_message: Optional[str]


class CareRequestRelated(CareRequestCreate):
    postulation_id: UUID
    pet_id: UUID

    class Config:
        orm_mode = True

class CareRequestOut(CareRequestRelated):
    id: UUID

    class Config:
        orm_mode = True
