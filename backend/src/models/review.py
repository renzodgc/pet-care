import typing
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import DatedTableMixin, SQLBase

if typing.TYPE_CHECKING:
    from src.models import User
    from src.models import Pet


class BaseReview(SQLBase, DatedTableMixin):
    rate: Mapped[int]
    comment: Mapped[str]


class CaretakerReview(SQLBase, DatedTableMixin):
    reviewer_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))
    reviewer: Mapped["User"] = relationship("User", back_populates="submitted_caretaker_reviews")
    caretaker_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))
    caretaker: Mapped["User"] = relationship("User", back_populates="received_caretaker_reviews")


class PetReview(SQLBase, DatedTableMixin):
    reviewer_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))
    reviewer: Mapped["User"] = relationship("User", back_populates="submitted_pet_reviews")
    pet_id: Mapped[UUID] = mapped_column(ForeignKey("pet.id"))
    pet: Mapped["Pet"] = relationship("Pet", back_populates="reviews")
