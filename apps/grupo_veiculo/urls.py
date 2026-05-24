from django.urls import path
from . import views

app_name = 'grupo_veiculo'

urlpatterns = [
    path('', views.GrupoVeiculoListView.as_view(), name='lista'),
    path('novo/', views.GrupoVeiculoCreateView.as_view(), name='criar'),
    path('<int:pk>/', views.GrupoVeiculoDetailView.as_view(), name='detalhe'),
    path('<int:pk>/editar/', views.GrupoVeiculoUpdateView.as_view(), name='editar'),
    path('<int:pk>/excluir/', views.GrupoVeiculoDeleteView.as_view(), name='excluir'),
]