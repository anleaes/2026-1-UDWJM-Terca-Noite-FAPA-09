from django.urls import path

from .views import (
    VeiculoListView,
    VeiculoDetailView,
    VeiculoCreateView,
    VeiculoUpdateView,
    VeiculoDeleteView,
)


app_name = 'veiculo_web'


urlpatterns = [
    path('', VeiculoListView.as_view(), name='lista'),
    path('listar/', VeiculoListView.as_view(), name='listar'),
    path('novo/', VeiculoCreateView.as_view(), name='novo'),
    path('criar/', VeiculoCreateView.as_view(), name='criar'),
    path('<int:pk>/', VeiculoDetailView.as_view(), name='detalhe'),
    path('<int:pk>/editar/', VeiculoUpdateView.as_view(), name='editar'),
    path('<int:pk>/excluir/', VeiculoDeleteView.as_view(), name='excluir'),
    path('<int:pk>/deletar/', VeiculoDeleteView.as_view(), name='deletar'),
]