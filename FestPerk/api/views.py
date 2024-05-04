from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from .models import Travel, City, Club, Party, Participant, Traveler
from .serializers import (
    TravelSerializer,
    CitySerializer,
    ClubSerializer,
    PartySerializer,
    ParticipantSerializer,
)

from rest_framework.permissions import IsAuthenticated

class TravelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TravelSerializer

    @csrf_exempt
    def get_queryset(self):
        username = self.request.user.username
        return Travel.objects.filter(traveler__user__username=username)
    
    @csrf_exempt
    def create(self, request):
        body = request.data
        required_fields = ["city", "ini_date", "end_date"]
        for field in required_fields:
            if field not in body:
                return Response(
                    {"error": f"Missing required field: {field}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        traveler = Traveler.objects.get(user=request.user)
        city = City.objects.get(name=body["city"])
        travel = Travel.objects.create(
            city=city,
            ini_date=body["ini_date"],
            end_date=body["end_date"],
            traveler=traveler,
        )
        travel.save()
        return Response(
            data={"message": "Travel created correctly", "travel": travel.uuid},
            status=status.HTTP_201_CREATED,
        )


class CreateTravelView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, format=None):
        body = request.data
        required_fields = ["city", "ini_date", "end_date"]
        for field in required_fields:
            if field not in body:
                return Response(
                    {"error": f"Missing required field: {field}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        traveler = Traveler.objects.get(user=request.user)
        city = City.objects.get(name=body["city"])
        travel = Travel.objects.create(
            city=city,
            ini_date=body["ini_date"],
            end_date=body["end_date"],
            traveler=traveler,
        )
        travel.save()
        return Response(
            data={"message": "Travel created correctly", "travel": travel.uuid},
            status=status.HTTP_201_CREATED,
        )


class ParticipantViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ParticipantSerializer

    def get_queryset(self):
        queryset = Participant.objects.filter(traveler__user=self.request.user)
        return queryset


# The views below are not gonna be used probably (at least not at the moment)


class PartyViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = PartySerializer

    def get_queryset(self):
        username = self.request.user.username
        queryset = Travel.objects.filter(traveler__user__username=username)
        return queryset


class CityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all()
    serializer_class = CitySerializer


class ClubViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
