from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CatalogoViewSet


app_name = 'catalogo'

router = DefaultRouter()
router.register('catalogo', CatalogoViewSet, basename='catalogo')

urlpatterns = [
    path('', include(router.urls)),
]