from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets

from .forms import GrupoVeiculoForm
from .models import GrupoVeiculo
from .serializers import GrupoVeiculoSerializer


class GrupoVeiculoViewSet(viewsets.ModelViewSet):
    queryset = GrupoVeiculo.objects.all().order_by('nome')
    serializer_class = GrupoVeiculoSerializer


class GrupoVeiculoListView(ListView):
    model = GrupoVeiculo
    template_name = 'grupo_veiculo/lista.html'
    context_object_name = 'grupos'


class GrupoVeiculoDetailView(DetailView):
    model = GrupoVeiculo
    template_name = 'grupo_veiculo/detalhe.html'
    context_object_name = 'grupo'


class GrupoVeiculoCreateView(CreateView):
    model = GrupoVeiculo
    form_class = GrupoVeiculoForm
    template_name = 'grupo_veiculo/form.html'
    success_url = reverse_lazy('grupo_veiculo_web:lista')


class GrupoVeiculoUpdateView(UpdateView):
    model = GrupoVeiculo
    form_class = GrupoVeiculoForm
    template_name = 'grupo_veiculo/form.html'
    success_url = reverse_lazy('grupo_veiculo_web:lista')


class GrupoVeiculoDeleteView(DeleteView):
    model = GrupoVeiculo
    template_name = 'grupo_veiculo/confirmar_delete.html'
    success_url = reverse_lazy('grupo_veiculo_web:lista')
    context_object_name = 'grupo'