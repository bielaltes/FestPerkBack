def create_travels():
    import random
    from django.utils import timezone
    from api.models import City, Traveler, Travel

    cities = City.objects.all()
    travelers = Traveler.objects.all()
    travels = []
    for traveler in travelers:
        date = timezone.now().date()
        random_city = random.choice(cities)
        travels.append(
            Travel(city=random_city, traveler=traveler, ini_date=date, end_date=date)
        )
    Travel.objects.bulk_create(travels)


if __name__ == "__main__":
    from api.scripts.django_setup import django_setup

    django_setup()
    create_travels()
