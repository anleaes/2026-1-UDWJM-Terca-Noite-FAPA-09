from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LocalViewSet


app_name = 'locais_api'

router = DefaultRouter()
router.register('locais', LocalViewSet, basename='local')

urlpatterns = [
    path('', include(router.urls)),
]
