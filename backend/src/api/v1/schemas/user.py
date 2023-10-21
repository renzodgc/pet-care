from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    password: str


class UserCreate(UserBase):
    first_name: str
    last_name: str
    phone_number: str
    country: str
    city: str
    neighborhood: str


class User(UserBase):
    id: UUID
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True
