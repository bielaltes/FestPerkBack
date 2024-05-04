from rest_framework import serializers
from .models import Travel, City, Club, Party, Participant


class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = ["uuid", "city", "traveler", "ini_date", "end_date"]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["name"]


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ["uuid", "name", "city"]


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ["uuid", "club", "date"]


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ["uuid", "party", "traveler"]
