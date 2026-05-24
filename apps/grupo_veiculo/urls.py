from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import GrupoVeiculoViewSet


app_name = 'grupo_veiculo'

router = DefaultRouter()
router.register('grupos', GrupoVeiculoViewSet, basename='grupo')

urlpatterns = [
    path('', include(router.urls)),
]