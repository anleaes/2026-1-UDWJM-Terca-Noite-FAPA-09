from django.urls import path
from .views import (
    LocalListView,
    LocalDetailView,
    LocalCreateView,
    LocalUpdateView,
    LocalDeleteView,
)


app_name = 'locais'


urlpatterns = [
    path('', LocalListView.as_view(), name='lista'),
    path('listar/', LocalListView.as_view(), name='listar'),
    path('novo/', LocalCreateView.as_view(), name='novo'),
    path('criar/', LocalCreateView.as_view(), name='criar'),
    path('<int:pk>/', LocalDetailView.as_view(), name='detalhe'),
    path('<int:pk>/editar/', LocalUpdateView.as_view(), name='editar'),
    path('<int:pk>/excluir/', LocalDeleteView.as_view(), name='excluir'),
    path('<int:pk>/deletar/', LocalDeleteView.as_view(), name='deletar'),
]