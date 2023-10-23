from uuid import UUID

from src import models
from src.api.v1 import schemas
from src.core.database import Session


class CareRequestController:
    @staticmethod
    def create(
        care_request_data: schemas.CareRequestCreate, postulation_id: UUID, pet_id: UUID, session: Session
    ) -> models.CareRequest:
        care_request_data = schemas.CareRequestRelated(postulation_id=postulation_id, pet_id=pet_id, **care_request_data.dict())
        care_postulation = models.CareRequest.objects(session).create(care_request_data.dict())
        return care_postulation
