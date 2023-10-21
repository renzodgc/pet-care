import typing
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import DatedTableMixin, SQLBase

if typing.TYPE_CHECKING:
    from src.models import User
    from src.models import Pet

# TODO: Make abstract inheritance table
# class BaseReview(SQLBase, DatedTableMixin):
#     rate: Mapped[int]
#     comment: Mapped[str]
#     reviewer_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))
#     reviewer: Mapped["User"] = relationship("User", back_populates="submitted_caretaker_reviews", foreign_keys=[reviewer_id])


class CaretakerReview(SQLBase, DatedTableMixin):
    rate: Mapped[int]
    comment: Mapped[str]
    reviewer_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))
    reviewer: Mapped["User"] = relationship("User", back_populates="submitted_caretaker_reviews", foreign_keys=[reviewer_id])
    caretaker_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))
    caretaker: Mapped["User"] = relationship("User", back_populates="received_caretaker_reviews", foreign_keys=[caretaker_id])


class PetReview(SQLBase, DatedTableMixin):
    rate: Mapped[int]
    comment: Mapped[str]
    reviewer_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))
    reviewer: Mapped["User"] = relationship("User", back_populates="submitted_pet_reviews", foreign_keys=[reviewer_id])
    pet_id: Mapped[UUID] = mapped_column(ForeignKey("pet.id"))
    pet: Mapped["Pet"] = relationship("Pet", back_populates="reviews")
