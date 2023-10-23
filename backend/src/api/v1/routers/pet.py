from typing import Any
from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate

from src.models import Pet, User
from src.core.database import Session
from src.api.dependencies import db_session, get_user
from src.api.v1.schemas import PetOut

router = APIRouter()


@router.get("/my-pets", response_model=Page[PetOut])
def get_my_pets(
    user: User = Depends(get_user), session: Session = Depends(db_session)
) -> Any:
    return paginate(session, user.get_pets())


@router.get("", response_model=Page[PetOut])
def get_all_pets(user: User = Depends(get_user), session: Session = Depends(db_session)) -> Any:
    return paginate(session, user.get_all_pets())


@router.get("/{pet_id}", response_model=PetOut)
def get_a_pet(pet_id: UUID, user: User = Depends(get_user), session: Session = Depends(db_session)) -> Any:
    return Pet.objects(session).get_or_404(Pet.id == pet_id)
