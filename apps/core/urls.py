from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('veiculo/<int:pk>/', views.veiculo_detalhe, name='veiculo_detalhe'),
]