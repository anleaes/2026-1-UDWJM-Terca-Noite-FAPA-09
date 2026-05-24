from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SolicitacaoViewSet


app_name = 'solicitacoes_api'

router = DefaultRouter()
router.register('solicitacoes', SolicitacaoViewSet, basename='solicitacao')

urlpatterns = [
    path('', include(router.urls)),
]
