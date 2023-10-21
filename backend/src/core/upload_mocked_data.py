from src.models import User, Pet, CaretakerReview, PetReview, CarePostulation, CareRequest, Species

def upload_mocked_data():
    carla = User(
        email="carlamartinez@gmail.com",
        password="xmartlabs",
        first_name="Carla",
        last_name="Gonzalez",
        phone_number="099775514",
        country="Uruguay",
        city="Montevideo",
        neighborhood="Pocitos",
    )
    carla_pet = Pet(
        name="Ringo",
        specie=Species.dog,
        breed="Golden Retriever",
        description="Es un perro muy tranquilo y cariñoso",
        cautions="No le gusta que lo toquen mucho",
        owner=carla,
    )
    marta = User(
        email="marta@gmail.com",
        password="xmartlabs",
        first_name="Marta",
        last_name="Ramirez",
        phone_number="099931831",
        country="Uruguay",
        city="Montevideo",
        neighborhood="Pocitos",
    )
    marta_pet = Pet(
        name="Merlina",
        specie=Species.cat,
        breed=None,
        description="Es una gata muy juguetona",
        cautions="No le gusta que la toquen mucho",
        owner=marta,
    )

