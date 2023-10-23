from datetime import datetime
from src.core.database import SessionLocal
from src.models import User, Pet, CaretakerReview, PetReview, CarePostulation, CareRequest, Species
from src.api.dependencies import db_session
from src.api.v1.schemas import UserCreate, PetCreate, CarePostulationCreate, CareRequestCreate, ReviewCreate
from src.controllers import UserController, PetController, CarePostulationController, CareRequestController, ReviewController

session = SessionLocal()

def drop_mocked_data():
    session.query(PetReview).delete()
    session.query(CaretakerReview).delete()
    session.query(CareRequest).delete()
    session.query(Pet).delete()
    session.query(CarePostulation).delete()
    session.query(User).delete()

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
    carla_pet = PetController.create(
        pet_data=PetCreate(
            name="Teo",
            specie=Species.dog,
            breed="Perro Salchicha",
            description="Es un perro muy tranquilo y cariñoso",
            cautions="No le gusta que lo toquen mucho",
        ),
        owner_id=carla.id,
        session=session
    )
    marta_pet = PetController.create(
        pet_data=PetCreate(
            name="Merlina",
            specie=Species.cat,
            breed=None,
            description="Es una gata muy juguetona",
            cautions="No le gusta que la toquen mucho",
        ),
        owner_id=marta.id,
        session=session
    )
    marta_postulation = CarePostulationController.create(
        care_postulation_data=CarePostulationCreate(
            start_date=datetime(2024, 1, 10),
            end_date=datetime(2024, 3, 10),
            price_per_day=1500,
            restrictions="No perros grandes",
            place_traits="Tengo balcón con red",
            allowed_species=Species.dog,
        ),
        caretaker_id=marta.id,
        session=session
    )
    carla_request = CareRequestController.create(
        care_request_data=CareRequestCreate(
            start_date=datetime(2024, 1, 15),
            end_date=datetime(2024, 1, 25),
            request_message="Es necesario jugar con el 3 veces al día"
        ),
        postulation_id=marta_postulation.id,
        pet_id=carla_pet.id,
        session=session
    )
    marta_review = ReviewController.create_pet_review(
        review_data=ReviewCreate(
            rate=5,
            comment="Es hermoso el perrito. Super mimoso. Le gustaba mucho tirarse en el balcón al sol, y yo estaba segura porque tengo red",
        ),
        reviewer_id=marta.id,
        pet_id=carla_pet.id,
        session=session
    )
    carla_review = ReviewController.create_caretaker_review(
        review_data=ReviewCreate(
            rate=5,
            comment="Marta es una cuidadora excelente. Teo volvió muy contento y se notaba que lo habían cuidado muy bien",
        ),
        reviewer_id=carla.id,
        caretaker_id=marta.id,
        session=session
    )