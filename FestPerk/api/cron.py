
from .models import City

def cronfunction():
    print("hola")
    citi = City.objects.create(name="Andorra la vella")
    citi.save()