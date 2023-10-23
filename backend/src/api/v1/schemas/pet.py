from uuid import UUID

from pydantic import BaseModel
from src.models import Species

class PetCreate(BaseModel):
    name: str
    specie: Species
    breed: str | None
    description: str
    cautions: str

class PetOwner(PetCreate):
    owner_id: UUID

    class Config:
        orm_mode = True


class PetOut(PetOwner):
    id: UUID

    class Config:
        orm_mode = True
