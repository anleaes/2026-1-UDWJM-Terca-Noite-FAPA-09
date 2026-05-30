from django.urls import path

from .views import (
    ManutencaoCreateView,
    ManutencaoDeleteView,
    ManutencaoDetailView,
    ManutencaoListView,
    ManutencaoUpdateView,
    PecaCreateView,
    PecaDeleteView,
    PecaDetailView,
    PecaListView,
    PecaManutencaoCreateView,
    PecaManutencaoDeleteView,
    PecaManutencaoDetailView,
    PecaManutencaoListView,
    PecaManutencaoUpdateView,
    PecaUpdateView,
)


app_name = 'manutencao_web'


urlpatterns = [
    path('', ManutencaoListView.as_view(), name='lista'),
    path('listar/', ManutencaoListView.as_view(), name='listar'),
    path('novo/', ManutencaoCreateView.as_view(), name='novo'),
    path('criar/', ManutencaoCreateView.as_view(), name='criar'),
    path('<int:pk>/', ManutencaoDetailView.as_view(), name='detalhe'),
    path('<int:pk>/editar/', ManutencaoUpdateView.as_view(), name='editar'),
    path('<int:pk>/excluir/', ManutencaoDeleteView.as_view(), name='excluir'),
    path('<int:pk>/deletar/', ManutencaoDeleteView.as_view(), name='deletar'),
    path('pecas/', PecaListView.as_view(), name='pecas_lista'),
    path('pecas/listar/', PecaListView.as_view(), name='pecas_listar'),
    path('pecas/novo/', PecaCreateView.as_view(), name='pecas_novo'),
    path('pecas/criar/', PecaCreateView.as_view(), name='pecas_criar'),
    path('pecas/<int:pk>/', PecaDetailView.as_view(), name='pecas_detalhe'),
    path('pecas/<int:pk>/editar/', PecaUpdateView.as_view(), name='pecas_editar'),
    path('pecas/<int:pk>/excluir/', PecaDeleteView.as_view(), name='pecas_excluir'),
    path('pecas/<int:pk>/deletar/', PecaDeleteView.as_view(), name='pecas_deletar'),
    path('pecas-manutencao/', PecaManutencaoListView.as_view(), name='pecas_manutencao_lista'),
    path('pecas-manutencao/listar/', PecaManutencaoListView.as_view(), name='pecas_manutencao_listar'),
    path('pecas-manutencao/novo/', PecaManutencaoCreateView.as_view(), name='pecas_manutencao_novo'),
    path('pecas-manutencao/criar/', PecaManutencaoCreateView.as_view(), name='pecas_manutencao_criar'),
    path('pecas-manutencao/<int:pk>/', PecaManutencaoDetailView.as_view(), name='pecas_manutencao_detalhe'),
    path('pecas-manutencao/<int:pk>/editar/', PecaManutencaoUpdateView.as_view(), name='pecas_manutencao_editar'),
    path('pecas-manutencao/<int:pk>/excluir/', PecaManutencaoDeleteView.as_view(), name='pecas_manutencao_excluir'),
    path('pecas-manutencao/<int:pk>/deletar/', PecaManutencaoDeleteView.as_view(), name='pecas_manutencao_deletar'),
]
