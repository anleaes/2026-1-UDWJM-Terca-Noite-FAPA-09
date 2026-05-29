from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets

from .forms import VeiculoForm
from .models import Veiculo
from .serializers import VeiculoSerializer


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.select_related('grupo').all().order_by('placa')
    serializer_class = VeiculoSerializer


class VeiculoListView(ListView):
    model = Veiculo
    template_name = 'veiculo/lista.html'
    context_object_name = 'veiculos'


class VeiculoDetailView(DetailView):
    model = Veiculo
    template_name = 'veiculo/detalhe.html'
    context_object_name = 'veiculo'


class VeiculoCreateView(CreateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = 'veiculo/form.html'
    success_url = reverse_lazy('veiculo_web:lista')


class VeiculoUpdateView(UpdateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = 'veiculo/form.html'
    success_url = reverse_lazy('veiculo_web:lista')


class VeiculoDeleteView(DeleteView):
    model = Veiculo
    template_name = 'veiculo/confirmar_delete.html'
    success_url = reverse_lazy('veiculo_web:lista')
    context_object_name = 'veiculo'