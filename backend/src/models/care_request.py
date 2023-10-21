import typing
from enum import auto, StrEnum
from datetime import datetime
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import DatedTableMixin, SQLBase

if typing.TYPE_CHECKING:
    from src.models import Pet, CarePostulation


class CareRequestStatus(StrEnum):
    pending = auto()
    accepted = auto()
    rejected = auto()


class CareRequest(SQLBase, DatedTableMixin):
    status: Mapped[CareRequestStatus] = mapped_column(CareRequestStatus, default=CareRequestStatus.pending)
    start_date: Mapped[datetime]
    end_date: Mapped[datetime]
    request_message: Mapped[str]
    response_message: Mapped[str | None]
    pet_id: Mapped[UUID] = mapped_column(ForeignKey("pet.id"))
    pet: Mapped["Pet"] = relationship("Pet", back_populates="requests")
    postulation_id: Mapped[UUID] = mapped_column(ForeignKey("care_postulation.id"))
    postulation: Mapped["CarePostulation"] = relationship("CarePostulation", back_populates="requests")
