from django.urls import include, path


app_name = 'api'

urlpatterns = [
    path('', include('manutencao.urls', namespace='manutencao')),
]
