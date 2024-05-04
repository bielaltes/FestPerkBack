def create_travelers():
    from django.contrib.auth.hashers import make_password

    from django.contrib.auth.models import User
    from api.models import Traveler

    users = []
    travelers = []
    for i in range(100):
        user = User(username=f"user{i}", password=make_password(f"user{i}"))
        users.append(user)
        travelers.append(Traveler(user=user, age=20 + i % 10))
    User.objects.bulk_create(users)
    Traveler.objects.bulk_create(travelers)


if __name__ == "__main__":
    from api.scripts.django_setup import django_setup

    django_setup()
    create_travelers()
