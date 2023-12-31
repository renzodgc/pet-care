import typing
from datetime import datetime
from enum import auto, StrEnum
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import DatedTableMixin, SQLBase
 
if typing.TYPE_CHECKING:
    from src.models import User, CareRequest
from src.models.pet import Species


class CarePostulation(SQLBase, DatedTableMixin):
    start_date: Mapped[datetime]
    end_date: Mapped[datetime]
    price_per_day: Mapped[int]
    restrictions: Mapped[str]
    allowed_species: Mapped[Species]# TODO: [typing.List[Species]]
    place_traits: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)
    caretaker_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))
    caretaker: Mapped["User"] = relationship("User", back_populates="care_postulations")
    care_requests: Mapped["CareRequest"] = relationship("CareRequest", back_populates="postulation")
