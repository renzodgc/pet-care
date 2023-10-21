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
    password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    phone_number: Mapped[str]
    country: Mapped[str]
    city: Mapped[str]
    neighborhood: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    pets: Mapped[List["Pet"]] = relationship("Pet", back_populates="owner")
    submitted_caretaker_reviews: Mapped[List["CaretakerReview"]] = relationship(
        "CaretakerReview", back_populates="reviewer", foreign_keys="CaretakerReview.reviewer_id"
    )

    # Caretaker
    care_postulations: Mapped[List["CarePostulation"]] = relationship("CarePostulation", back_populates="caretaker")
    submitted_pet_reviews: Mapped[List["PetReview"]] = relationship("PetReview", back_populates="reviewer")
    received_caretaker_reviews: Mapped[List["CaretakerReview"]] = relationship(
        "CaretakerReview", back_populates="caretaker", foreign_keys="CaretakerReview.caretaker_id"
    )

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    # def __str__(self) -> str:
    #     return self.email

    @classmethod
    def actives(cls, session: Session) -> Objects["User"]:
        return Objects(cls, session, User.is_active == True)  # noqa: E712

    def get_my_pets(self) -> Select:
        from src.models import Pet

        statement = select(Pet).filter(Pet.owner_id == self.id).filter(Pet.is_active == True)  # noqa: E712
        return statement

    def get_all_pets(self) -> Select:
        from src.models import Pet
        
        statement = select(Pet).filter(Pet.is_active == True)  # noqa: E712
        return statement

    def get_a_pet(self) -> Select:
        from src.models import Pet

        statement = select(Pet).filter(Pet.id == self.id).filter(Pet.is_active == True)  # noqa: E712
        return statement

    def get_my_care_postulations(self) -> Select:
        from src.models import CarePostulation

        statement = select(CarePostulation).filter(CarePostulation.caretaker_id == self.id).filter(CarePostulation.is_active == True)  # noqa: E712
        return statement

    def get_all_care_postulations(self) -> Select:
        from src.models import CarePostulation
        
        statement = select(CarePostulation).filter(CarePostulation.is_active == True)  # noqa: E712
        return statement

    def get_a_care_postulation(self) -> Select:
        from src.models import CarePostulation

        statement = select(CarePostulation).filter(CarePostulation.id == self.id).filter(CarePostulation.is_active == True)  # noqa: E712
        return statement
