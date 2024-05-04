def create_cities():
    from api.models import City

    cities_to_create = ["Barcelona", "London", "Paris"]

    cities = []
    for city in cities_to_create:
        cities.append(City(name=city))
    City.objects.bulk_create(cities)


if __name__ == "__main__":
    from api.scripts.django_setup import django_setup

    django_setup()
    create_cities()
