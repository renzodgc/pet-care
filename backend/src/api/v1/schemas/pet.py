from uuid import UUID

from pydantic import BaseModel
from src.models import Species

class PetCreate(BaseModel):
    name: str
    specie: Species
    breed: str | None
    description: str
    cautions: str

class PetOut(BaseModel):
    pet_id: UUID
    name: str
    description: str
    cautions: str
    breed: str | None

    class Config:
        orm_mode = True
