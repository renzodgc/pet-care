from datetime import datetime
from src.core.database import SessionLocal
from src.models import User, Pet, CaretakerReview, PetReview, CarePostulation, CareRequest, Species
from src.api.dependencies import db_session
from src.api.v1.schemas import UserCreate
from src.controllers import UserController

session = SessionLocal()

def drop_mocked_data():
    session.query(Pet).delete()
    session.query(User).delete()
    session.query(CarePostulation).delete()
    session.query(CareRequest).delete()
    session.query(PetReview).delete()
    session.query(CaretakerReview).delete()

def upload_mocked_data():
    carla = UserController.create(
        user_data=UserCreate(
            email="carlamartinez@gmail.com",
            password="xmartlabs",
            first_name="Carla",
            last_name="Gonzalez",
            phone_number="099775514",
            country="Uruguay",
            city="Montevideo",
            neighborhood="Pocitos",
        ),
        session=session
    )
    marta = UserController.create(
        user_data=UserCreate(
            email="marta@xmartlabs.com",
            password="xmartlabs",
            first_name="Marta",
            last_name="Ramirez",
            phone_number="099931831",
            country="Uruguay",
            city="Montevideo",
            neighborhood="Pocitos",
        ),
        session=session
    )
    # carla_pet = Pet.objects(session).create({
    #     "name": "Teo",
    #     "specie": Species.dog,
    #     "breed": "Perro Salchicha",
    #     "description": "Es un perro muy tranquilo y cariñoso",
    #     "cautions": "No le gusta que lo toquen mucho",
    #     "owner_id": carla.id,
    # })
    # marta_pet = Pet.objects(session).create({
    #     "name": "Merlina",
    #     "specie": Species.cat,
    #     "breed": None,
    #     "description": "Es una gata muy juguetona",
    #     "cautions": "No le gusta que la toquen mucho",
    #     "owner_id": marta.id,
    # })
