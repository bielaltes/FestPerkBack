from rest_framework import viewsets
from .models import Travels, City, Local, Party, Participant
from .serializers import (
    TravelsSerializer,
    CitySerializer,
    LocalSerializer,
    PartySerializer,
    ParticipantSerializer,
)


class TravelsViewSet(viewsets.ModelViewSet):
    queryset = Travels.objects.all()
    serializer_class = TravelsSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
