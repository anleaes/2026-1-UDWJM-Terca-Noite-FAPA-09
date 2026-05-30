from django.urls import path

from .views import (
    ManutencaoCreateView,
    ManutencaoDeleteView,
    ManutencaoDetailView,
    ManutencaoListView,
    ManutencaoUpdateView,
)


app_name = 'manutencao_web'


urlpatterns = [
    path('', ManutencaoListView.as_view(), name='lista'),
    path('listar/', ManutencaoListView.as_view(), name='listar'),
    path('nova/', ManutencaoCreateView.as_view(), name='nova'),
    path('criar/', ManutencaoCreateView.as_view(), name='criar'),
    path('<int:pk>/', ManutencaoDetailView.as_view(), name='detalhe'),
    path('<int:pk>/editar/', ManutencaoUpdateView.as_view(), name='editar'),
    path('<int:pk>/excluir/', ManutencaoDeleteView.as_view(), name='excluir'),
    path('<int:pk>/deletar/', ManutencaoDeleteView.as_view(), name='deletar'),
]
