from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, FuncionarioViewSet


app_name = 'users'

router = DefaultRouter()
router.register('clientes', ClienteViewSet, basename='cliente')
router.register('funcionarios', FuncionarioViewSet, basename='funcionario')


urlpatterns = [
    path('', include(router.urls)),
]