import typing
from enum import StrEnum, auto
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import DatedTableMixin, SQLBase


if typing.TYPE_CHECKING:
    from src.models import User, PetReview, CareRequest


class Species(StrEnum):
    dog = auto()
    cat = auto()


class Pet(SQLBase, DatedTableMixin):
    name: Mapped[str]
    specie: Mapped[Species]
    breed: Mapped[str | None]
    description: Mapped[str]
    cautions: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)
    owner_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))
    owner: Mapped["User"] = relationship("User", back_populates="pets")
    reviews: Mapped["PetReview"] = relationship("PetReview", back_populates="pet")
    care_requests: Mapped["CareRequest"] = relationship("CareRequest", back_populates="pet")

    def __str__(self) -> str:
        return f"Item {str(self.id)[:12]}..."
