from uuid import UUID

from pydantic import BaseModel


class PetOut(BaseModel):
    pet_id: UUID
    name: str
    description: str
    cautions: str
    breed: str | None

    class Config:
        orm_mode = True
