from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Traveler


@receiver(post_save, sender=User)
def create_user_traveler(sender, instance, created, **kwargs):
    if created:
        Traveler.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.traveler.save()
