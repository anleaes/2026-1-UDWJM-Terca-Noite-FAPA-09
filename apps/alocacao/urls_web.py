from django.urls import path

from .views import (
    AlocacaoListView,
    AlocacaoDetailView,
    AlocacaoCreateView,
    AlocacaoUpdateView,
    AlocacaoDeleteView,
    HistoricoAlocacaoListView,
)


app_name = 'alocacao_web'


urlpatterns = [
    path('', AlocacaoListView.as_view(), name='lista'),
    path('nova/', AlocacaoCreateView.as_view(), name='criar'),
    path('<int:pk>/', AlocacaoDetailView.as_view(), name='detalhe'),
    path('<int:pk>/editar/', AlocacaoUpdateView.as_view(), name='editar'),
    path('<int:pk>/excluir/', AlocacaoDeleteView.as_view(), name='excluir'),

    path('historicos/', HistoricoAlocacaoListView.as_view(), name='historicos'),
]