from uuid import UUID

from src import models
from src.api.v1 import schemas
from src.core.database import Session


class PetController:
    @staticmethod
    def create(
        pet_data: schemas.PetCreate, owner_id: UUID, session: Session
    ) -> models.Pet:
        pet_data = schemas.PetCreate(owner_id=owner_id, **pet_data.dict())
        pet = models.Pet.objects(session).create(pet_data.dict())
        return pet
