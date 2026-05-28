from django.urls import path

from .views import (
    FuncionarioListView,
    FuncionarioDetailView,
    FuncionarioCreateView,
    FuncionarioUpdateView,
    FuncionarioDeleteView,
)


app_name = 'users_web'


urlpatterns = [

    path('funcionarios/', FuncionarioListView.as_view(), name='funcionarios_lista'),
    path('funcionarios/listar/', FuncionarioListView.as_view(), name='funcionarios_listar'),
    path('funcionarios/novo/', FuncionarioCreateView.as_view(), name='funcionarios_novo'),
    path('funcionarios/criar/', FuncionarioCreateView.as_view(), name='funcionarios_criar'),
    path('funcionarios/<int:pk>/', FuncionarioDetailView.as_view(), name='funcionarios_detalhe'),
    path('funcionarios/<int:pk>/editar/', FuncionarioUpdateView.as_view(), name='funcionarios_editar'),
    path('funcionarios/<int:pk>/excluir/', FuncionarioDeleteView.as_view(), name='funcionarios_excluir'),
    path('funcionarios/<int:pk>/deletar/', FuncionarioDeleteView.as_view(), name='funcionarios_deletar'),
]