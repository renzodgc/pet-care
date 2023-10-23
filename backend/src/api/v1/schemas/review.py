from typing import Optional
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class ReviewCreate(BaseModel):
    rate: int
    comment: str

class ReviewRelated(ReviewCreate):
    reviewer_id: UUID

    class Config:
        orm_mode = True

class PetReviewRelated(ReviewRelated):
    pet_id: UUID

    class Config:
        orm_mode = True

class CaretakerReviewRelated(ReviewRelated):
    caretaker_id: UUID

    class Config:
        orm_mode = True
