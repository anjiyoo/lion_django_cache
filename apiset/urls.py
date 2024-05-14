from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()  # DefaultRouter 인스턴스를 생성

router.register(r'products', ProductViewSet)  # ProductViewSet 클래스를 products URL에 등록

urlpatterns = [
    path('', include(router.urls)),  # products/ 와 같은 형태로 자동으로 생성
]