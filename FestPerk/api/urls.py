from django.urls import path, include
from rest_framework import routers
from .views import (
    TravelViewSet,
    CityViewSet,
    ClubViewSet,
    PartyViewSet,
    ParticipantViewSet,
)

router = routers.DefaultRouter()
router.register(r"travels", TravelViewSet)
router.register(r"cities", CityViewSet)
router.register(r"clubs", ClubViewSet)
router.register(r"parties", PartyViewSet)
router.register(r"participants", ParticipantViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
