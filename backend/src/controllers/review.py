from uuid import UUID

from src import models
from src.api.v1 import schemas
from src.core.database import Session


class ReviewController:
    @staticmethod
    def create_pet_review(
        review_data: schemas.ReviewCreate, reviewer_id: UUID, pet_id: UUID, session: Session
    ) -> models.PetReview:
        review_data = schemas.PetReviewRelated(reviewer_id=reviewer_id, pet_id=pet_id, **review_data.dict())
        review = models.PetReview.objects(session).create(review_data.dict())
        return review

    @staticmethod
    def create_caretaker_review(
        review_data: schemas.ReviewCreate, reviewer_id: UUID, caretaker_id: UUID, session: Session
    ) -> models.CaretakerReview:
        review_data = schemas.CaretakerReviewRelated(reviewer_id=reviewer_id, caretaker_id=caretaker_id, **review_data.dict())
        review = models.CaretakerReview.objects(session).create(review_data.dict())
        return review
