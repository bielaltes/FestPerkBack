def create_travels():
    import random
    from django.utils import timezone
    from api.models import City, Traveller, Travels

    cities = City.objects.all()
    users = Traveller.objects.all()
    travels = []
    for user in users:
        date = timezone.now().date()
        random_city = random.choice(cities)
        travels.append(
            Travels(city=random_city, user=user, ini_date=date, end_date=date)
        )
    Travels.objects.bulk_create(travels)


if __name__ == "__main__":
    from api.scripts.django_setup import django_setup

    django_setup()
    create_travels()
