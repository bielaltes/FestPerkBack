def create_travellers():
    from django.contrib.auth.models import User
    from api.models import Traveller

    django_users = []
    my_users = []
    for i in range(100):
        user = User(username=f"user{i}", password=f"user{i}")
        django_users.append(user)
        my_users.append(Traveller(user=user, age=20 + i % 10))
    User.objects.bulk_create(django_users)
    Traveller.objects.bulk_create(my_users)


if __name__ == "__main__":
    from api.scripts.django_setup import django_setup

    django_setup()
    create_travellers()
