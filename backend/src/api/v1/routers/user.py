from typing import Any
from uuid import UUID

from fastapi import APIRouter, Depends, Response
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate

from src import models
from src.api.dependencies import db_session, get_user
from src.api.v1 import schemas
from src.api.v1.schemas import Token, UserCreate, UserBase
from src.controllers import UserController
from src.core.database import Session
from src.core.security import AuthManager

router = APIRouter()


@router.post("", status_code=201)
def signup(
    response: Response,
    user_data: UserCreate,
    session: Session = Depends(db_session),
) -> Token | None:
    user = UserController.create(user_data=user_data, session=session)
    return AuthManager.process_login(user=user, response=response)


@router.post("/login")
def login(
    response: Response,
    user_data: UserBase,
    session: Session = Depends(db_session),
) -> Token | None:
    user = UserController.login(user_data=user_data, session=session)
    return AuthManager.process_login(user=user, response=response)


@router.get("/me", response_model=schemas.UserOut)
def me(user: models.User = Depends(get_user)) -> Any:
    return user

@router.get("/{user_id}", response_model=schemas.UserOut)
def get_users(user_id: UUID, session: Session = Depends(db_session)) -> Any:
    user = models.User.objects(session).get_or_404(models.User.id == user_id)
    return user

@router.get("/{user_id}/pets", response_model=Page[schemas.PetOut])
def get_pets(user_id: UUID, session: Session = Depends(db_session)) -> Any:
    user = models.User.objects(session).get_or_404(models.User.id == user_id)
    return paginate(session, user.get_pets())
