from django.urls import path, include
from rest_framework import routers
from .views import (
    TravelsViewSet,
    CityViewSet,
    LocalViewSet,
    PartyViewSet,
    ParticipantViewSet,
)

router = routers.DefaultRouter()
router.register(r"travels", TravelsViewSet)
router.register(r"cities", CityViewSet)
router.register(r"locals", LocalViewSet)
router.register(r"parties", PartyViewSet)
router.register(r"participants", ParticipantViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
