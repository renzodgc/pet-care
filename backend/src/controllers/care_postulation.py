from uuid import UUID

from src import models
from src.api.v1 import schemas
from src.core.database import Session


class CarePostulationController:
    @staticmethod
    def create(
        care_postulation_data: schemas.CarePostulationCreate, caretaker_id: UUID, session: Session
    ) -> models.CareRequest:
        care_postulation_data = schemas.CarePostulationRelated(caretaker_id=caretaker_id, **care_postulation_data.dict())
        care_postulation = models.CarePostulation.objects(session).create(care_postulation_data.dict())
        return care_postulation
