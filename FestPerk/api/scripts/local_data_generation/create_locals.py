def create_locals():
    from api.models import Local, City

    locals_to_create = [
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

    locals = []
    cities = City.objects.all()
    cities_dict = {city.name: city for city in cities}
    for local in locals_to_create:
        locals.append(Local(name=local["name"], city=cities_dict[local["city_name"]]))
    Local.objects.bulk_create(locals)


if __name__ == "__main__":
    from api.scripts.django_setup import django_setup

    django_setup()
    create_locals()
