from rest_framework import serializers
from .models import Travel, City, Club, Party, Participant


class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = ["uuid", "city", "ini_date", "end_date"]


class ClubSerializer(serializers.ModelSerializer):
    club_uuid = serializers.UUIDField(source='uuid')

    class Meta:
        model = Club
        fields = ["club_uuid", "name", "city"]


class PartySerializer(serializers.ModelSerializer):
    party_uuid = serializers.UUIDField(source='uuid')
    club = ClubSerializer()

    class Meta:
        model = Party
        fields = ["party_uuid", "club", "date"]


class ParticipantSerializer(serializers.ModelSerializer):
    party_uuid = serializers.UUIDField(source='party.uuid', read_only=True)
    club_uuid = serializers.UUIDField(source='party.club.uuid', read_only=True)
    club_name = serializers.CharField(source='party.club.name', read_only=True)
    club_city = serializers.CharField(source='party.club.city.name', read_only=True)
    party_date = serializers.DateField(source='party.date', read_only=True)
    participant_uuid = serializers.UUIDField(source='uuid', read_only=True)
    traveler_uuid = serializers.UUIDField(source='traveler.uuid', read_only=True)

    class Meta:
        model = Participant
        fields = ["participant_uuid", "party_uuid", "club_uuid", "club_name", "club_city", "party_date", "traveler_uuid"]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["name"]
