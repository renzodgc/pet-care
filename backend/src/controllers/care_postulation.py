from uuid import UUID

from src import models
from src.api.v1 import schemas
from src.core.database import Session


class CarePostulationController:
    @staticmethod
    def create(
        item_data: schemas.UserCreate, owner_id: UUID, session: Session
    ) -> models.CarePostulation:
        pass
