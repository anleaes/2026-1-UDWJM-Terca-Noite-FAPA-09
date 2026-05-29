from django.urls import path
from .views import (
    SolicitacaoListView,
    SolicitacaoDetailView,
    SolicitacaoCreateView,
    SolicitacaoUpdateView,
    SolicitacaoDeleteView,
)


app_name = 'solicitacoes'


urlpatterns = [
    path('', SolicitacaoListView.as_view(), name='lista'),
    path('nova/', SolicitacaoCreateView.as_view(), name='criar'),
    path('<int:pk>/', SolicitacaoDetailView.as_view(), name='detalhe'),
    path('<int:pk>/editar/', SolicitacaoUpdateView.as_view(), name='editar'),
    path('<int:pk>/excluir/', SolicitacaoDeleteView.as_view(), name='excluir'),
]