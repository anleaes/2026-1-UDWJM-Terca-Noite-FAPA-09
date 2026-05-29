from django.urls import path

from .views import (
    CatalogoListView,
    CatalogoDetailView,
    CatalogoCreateView,
    CatalogoUpdateView,
    CatalogoDeleteView,
)


app_name = 'catalogo_web'


urlpatterns = [
    path('', CatalogoListView.as_view(), name='lista'),
    path('listar/', CatalogoListView.as_view(), name='listar'),
    path('novo/', CatalogoCreateView.as_view(), name='novo'),
    path('criar/', CatalogoCreateView.as_view(), name='criar'),
    path('<int:pk>/', CatalogoDetailView.as_view(), name='detalhe'),
    path('<int:pk>/editar/', CatalogoUpdateView.as_view(), name='editar'),
    path('<int:pk>/excluir/', CatalogoDeleteView.as_view(), name='excluir'),
    path('<int:pk>/deletar/', CatalogoDeleteView.as_view(), name='deletar'),
]