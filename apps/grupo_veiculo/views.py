from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import GrupoVeiculo
from .forms import GrupoVeiculoForm


class GrupoVeiculoListView(ListView):
    model = GrupoVeiculo
    template_name = 'grupo_veiculo/lista.html'
    context_object_name = 'grupos'
    ordering = ['nome']


class GrupoVeiculoDetailView(DetailView):
    model = GrupoVeiculo
    template_name = 'grupo_veiculo/detalhe.html'
    context_object_name = 'grupo'


class GrupoVeiculoCreateView(CreateView):
    model = GrupoVeiculo
    form_class = GrupoVeiculoForm
    template_name = 'grupo_veiculo/form.html'
    success_url = reverse_lazy('grupo_veiculo:lista')


class GrupoVeiculoUpdateView(UpdateView):
    model = GrupoVeiculo
    form_class = GrupoVeiculoForm
    template_name = 'grupo_veiculo/form.html'
    success_url = reverse_lazy('grupo_veiculo:lista')


class GrupoVeiculoDeleteView(DeleteView):
    model = GrupoVeiculo
    template_name = 'grupo_veiculo/confirmar_exclusao.html'
    context_object_name = 'grupo'
    success_url = reverse_lazy('grupo_veiculo:lista')