def create_all():
    from FestPerk.api.scripts.local_data_generation.create_travellers import create_travellers
    from api.scripts.local_data_generation.create_cities import create_cities
    from api.scripts.local_data_generation.create_locals import create_locals
    from api.scripts.local_data_generation.create_travels import create_travels

    create_travellers()
    create_cities()
    create_travels()
    create_locals()


if __name__ == "__main__":
    from api.scripts.django_setup import django_setup

    django_setup()
    create_all()
