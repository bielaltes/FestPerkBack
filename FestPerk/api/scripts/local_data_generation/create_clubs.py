def create_clubs():
    from api.models import Club, City

    clubs_to_create = [
        {"name": "Razzmatazz", "city_name": "Barcelona"},
        {"name": "Apolo", "city_name": "Barcelona"},
        {"name": "Coyote", "city_name": "Barcelona"},
        {"name": "LondonDisco", "city_name": "London"},
        {"name": "LondonGay", "city_name": "London"},
        {"name": "LondonBar", "city_name": "London"},
        {"name": "ParisDisco", "city_name": "Paris"},
        {"name": "ParisGay", "city_name": "Paris"},
        {"name": "ParisBar", "city_name": "Paris"},
    ]

    clubs = []
    cities = City.objects.all()
    cities_dict = {city.name: city for city in cities}
    for club in clubs_to_create:
        clubs.append(Club(name=club["name"], city=cities_dict[club["city_name"]]))
    Club.objects.bulk_create(clubs)


if __name__ == "__main__":
    from api.scripts.django_setup import django_setup

    django_setup()
    create_clubs()
