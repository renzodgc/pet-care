from uuid import UUID

from src import models
from src.api.v1 import schemas
from src.core.database import Session


class ReviewController:
    @staticmethod
    def create_pet_review(
        item_data: schemas.UserCreate, owner_id: UUID, session: Session
    ) -> models.PetReview:
        pass
        # item_data = schemas.Item(owner_id=owner_id, **item_data.dict())
        # item = models.Item.objects(session).create(item_data.dict())
        # return item

    @staticmethod
    def create_caretaker_review(
        item_data: schemas.UserCreate, owner_id: UUID, session: Session
    ) -> models.CaretakerReview:
        pass
