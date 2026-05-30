from django.urls import path

from .views import (
    AlocacaoListView,
    AlocacaoDetailView,
    AlocacaoCreateView,
    AlocacaoUpdateView,
    AlocacaoDeleteView,
    AlocacaoCancelarView,
    AlocacaoFinalizarView,
    HistoricoAlocacaoListView,
)


app_name = 'alocacao_web'


urlpatterns = [
    path('', AlocacaoListView.as_view(), name='lista'),
    path('listar/', AlocacaoListView.as_view(), name='listar'),
    path('nova/', AlocacaoCreateView.as_view(), name='nova'),
    path('criar/', AlocacaoCreateView.as_view(), name='criar'),
    path('<int:pk>/', AlocacaoDetailView.as_view(), name='detalhe'),
    path('<int:pk>/editar/', AlocacaoUpdateView.as_view(), name='editar'),
    path('<int:pk>/excluir/', AlocacaoDeleteView.as_view(), name='excluir'),
    path('<int:pk>/deletar/', AlocacaoDeleteView.as_view(), name='deletar'),
    path('<int:pk>/finalizar/', AlocacaoFinalizarView.as_view(), name='finalizar'),
    path('<int:pk>/cancelar/', AlocacaoCancelarView.as_view(), name='cancelar'),

    path('historicos/', HistoricoAlocacaoListView.as_view(), name='historicos'),
]
