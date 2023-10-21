from fastapi import APIRouter

from src.api.v1.routers import item, user, pet, care_postulation

v1_router = APIRouter()
v1_router.include_router(user.router, prefix="/users")
v1_router.include_router(item.router, prefix="/items")
v1_router.include_router(pet.router, prefix="/pets")
v1_router.include_router(care_postulation.router, prefix="/care-postulations")
