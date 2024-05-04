from django.urls import path, include
from rest_framework import routers
from .views import (
    TravelViewSet,
    CityViewSet,
    ClubViewSet,
    PartyViewSet,
    ParticipantViewSet,
    CreateTravelView
)

router = routers.DefaultRouter()
router.register(r"travels", TravelViewSet, basename="travels")
router.register(r"cities", CityViewSet, basename="cities")
router.register(r"clubs", ClubViewSet, basename="clubs")
router.register(r"parties", PartyViewSet, basename="parties")
router.register(r"participants", ParticipantViewSet, basename="participants")

urlpatterns = [
    path("", include(router.urls)),
    path('travels/new', CreateTravelView.as_view(), name='create_travel'),
]
