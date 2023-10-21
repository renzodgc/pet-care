from typing import Any
from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate

from src.models import CarePostulation, User
from src.core.database import Session
from src.api.dependencies import db_session, get_user
from src.api.v1.schemas import CarePostulationOut

router = APIRouter()


@router.get("/my-care-postulations", response_model=Page[CarePostulationOut])
def get_my_care_postulations(
    user: User = Depends(get_user), session: Session = Depends(db_session)
) -> Any:
    return paginate(session, user.get_my_care_postulations())


@router.get("", response_model=Page[CarePostulationOut])
def get_all_care_postulations(user: User = Depends(get_user), session: Session = Depends(db_session)) -> Any:
    return paginate(session, user.get_all_care_postulations())


@router.get("/{care_postulation_id}", response_model=CarePostulationOut)
def get_a_care_postulation(care_postulation_id: UUID, user: User = Depends(get_user), session: Session = Depends(db_session)) -> Any:
    return CarePostulation.objects(session).get_or_404(CarePostulation.id == care_postulation_id)
