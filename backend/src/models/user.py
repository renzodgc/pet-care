import typing
from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import Select

from src.core.database import DatedTableMixin, Objects, Session, SQLBase

if typing.TYPE_CHECKING:
    from src.models import Pet, CarePostulation, PetReview, CaretakerReview


class User(SQLBase, DatedTableMixin):
    email: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    pets: Mapped[List["Pet"]] = relationship("Pet", back_populates="owner")
    received_pet_reviews: Mapped[List["PetReview"]] = relationship()
    submitted_caretaker_reviews: Mapped[List["CaretakerReview"]] = relationship()

    # Caretaker
    care_postulations: Mapped[List["CarePostulation"]] = relationship("CarePostulation", back_populates="caretaker")
    submitted_pet_reviews: Mapped[List["PetReview"]] = relationship()
    received_caretaker_reviews: Mapped[List["CaretakerReview"]] = relationship()

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.email

    @classmethod
    def actives(cls, session: Session) -> Objects["User"]:
        return Objects(cls, session, User.is_active == True)  # noqa: E712

    def get_pets(self) -> Select:
        from src.models import Pet

        statement = select(Pet).filter(Pet.owner_id == self.id).filter(Pet.is_active == True)  # noqa: E712
        return statement
