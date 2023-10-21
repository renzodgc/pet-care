from uuid import UUID

from src import models
from src.api.v1 import schemas
from src.core.database import Session


class PetController:
    @staticmethod
    def create(
        item_data: schemas.ItemCreate, owner_id: UUID, session: Session
    ) -> models.Pet:
        pass
