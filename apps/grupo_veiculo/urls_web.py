from django.urls import path

from .views import (
    GrupoVeiculoListView,
    GrupoVeiculoDetailView,
    GrupoVeiculoCreateView,
    GrupoVeiculoUpdateView,
    GrupoVeiculoDeleteView,
)


app_name = 'grupo_veiculo_web'


urlpatterns = [
    path('', GrupoVeiculoListView.as_view(), name='lista'),
    path('listar/', GrupoVeiculoListView.as_view(), name='listar'),
    path('novo/', GrupoVeiculoCreateView.as_view(), name='novo'),
    path('criar/', GrupoVeiculoCreateView.as_view(), name='criar'),
    path('<int:pk>/', GrupoVeiculoDetailView.as_view(), name='detalhe'),
    path('<int:pk>/editar/', GrupoVeiculoUpdateView.as_view(), name='editar'),
    path('<int:pk>/excluir/', GrupoVeiculoDeleteView.as_view(), name='excluir'),
    path('<int:pk>/deletar/', GrupoVeiculoDeleteView.as_view(), name='deletar'),
]