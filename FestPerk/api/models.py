import uuid
from collections import defaultdict

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Traveler(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0, message="Age must be between 0 and 99."),
            MaxValueValidator(99, message="Age must be between 0 and 99."),
        ],
    )


class City(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

    class Meta:
        verbose_name_plural = "Cities"


class ClubManager(models.Manager):
    def get_clubs_by_city(self):
        clubs = Club.objects.all()
        clubs_by_city = defaultdict(list)

        for club in clubs:
            clubs_by_city[club.city.name].append(club)

        return clubs_by_city


class Club(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    objects = ClubManager()

    class Meta:
        unique_together = ("name", "city")


class Travel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE)
    ini_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        unique_together = ("traveler", "ini_date")


class Party(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    club = models.ForeignKey(Club, on_delete=models.PROTECT)
    date = models.DateField()

    class Meta:
        verbose_name_plural = "Parties"


class Participant(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    party = models.ForeignKey(Party, on_delete=models.PROTECT)
    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("party", "traveler")
