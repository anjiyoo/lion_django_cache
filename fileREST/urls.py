from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet, ImageViewSet

router = DefaultRouter()
router.register(r'documents', DocumentViewSet)  # http://127.0.0.1:8000/file/documents/
router.register(r'images', ImageViewSet)  # http://127.0.0.1:8000/file/images/

urlpatterns = [
    path('', include(router.urls)),
]