from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AlocacaoViewSet, HistoricoAlocacaoViewSet


app_name = 'alocacao'

router = DefaultRouter()
router.register('alocacoes', AlocacaoViewSet, basename='alocacao')
router.register('historicos-alocacao', HistoricoAlocacaoViewSet, basename='historico-alocacao')

urlpatterns = [
    path('', include(router.urls)),
]
