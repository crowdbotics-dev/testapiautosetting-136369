from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors136369ViewSet

router = DefaultRouter()
router.register(
    "testconnectors136369", Testconnectors136369ViewSet, basename="testconnectors136369"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
