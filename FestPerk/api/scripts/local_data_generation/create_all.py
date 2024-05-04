def create_all():
    from api.scripts.local_data_generation.create_travelers import create_travelers
    from api.scripts.local_data_generation.create_cities import create_cities
    from api.scripts.local_data_generation.create_clubs import create_clubs
    from api.scripts.local_data_generation.create_travels import create_travels

    create_travelers()
    create_cities()
    create_travels()
    create_clubs()


if __name__ == "__main__":
    from api.scripts.django_setup import django_setup

    django_setup()
    create_all()
