from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ManutencaoViewSet, PecaManutencaoViewSet, PecaViewSet


app_name = 'manutencao'

router = DefaultRouter()
router.register('manutencoes', ManutencaoViewSet, basename='manutencao')
router.register('pecas', PecaViewSet, basename='peca')
router.register('pecas-manutencao', PecaManutencaoViewSet, basename='peca-manutencao')

urlpatterns = [
    path('', include(router.urls)),
]
