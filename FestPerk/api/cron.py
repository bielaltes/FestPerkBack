
from django.contrib.auth.models import User


def cronfunction():
    print("hola")
    user = User.objects.create(username="carles", password="miquel")
    user.save()