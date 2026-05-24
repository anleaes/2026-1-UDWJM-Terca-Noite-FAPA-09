from django.urls import include, path


app_name = 'api'

urlpatterns = [
    path('', include('grupo_veiculo.urls', namespace='grupo_veiculo')),
    path('', include('veiculo.urls', namespace='veiculo')),
    path('', include('locais.urls_api', namespace='locais_api')),
    path('', include('solicitacoes.urls_api', namespace='solicitacoes_api')),
    path('', include('manutencao.urls', namespace='manutencao')),
]
