from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DocumentViewSet,
    ModelConfigViewSet,
    QueryExecutionViewSet,
    CanvasView,
)

router = DefaultRouter()
router.register(r"documents", DocumentViewSet)
router.register(r"models", ModelConfigViewSet)
router.register(r"queries", QueryExecutionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("canvas/", CanvasView.as_view(), name="canvas"),
]
