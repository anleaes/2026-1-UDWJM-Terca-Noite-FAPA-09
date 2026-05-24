from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import VeiculoViewSet


app_name = 'veiculo'

router = DefaultRouter()
router.register('veiculos', VeiculoViewSet, basename='veiculo')

urlpatterns = [
    path('', include(router.urls)),
]