import os
import django

# Use django settings 
def django_setup():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FestPerk.settings")
    django.setup()