from rest_framework import serializers
from .models import Travels, City, Local, Party, Participant


class TravelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travels
        fields = ["city", "user", "ini_date", "end_date"]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["name"]


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ["uuid", "name", "city"]


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ["id", "local", "date"]


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ["id", "party", "user"]
