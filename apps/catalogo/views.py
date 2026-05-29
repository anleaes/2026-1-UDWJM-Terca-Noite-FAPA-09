from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets

from .forms import CatalogoForm
from .models import Catalogo
from .serializers import CatalogoSerializer


class CatalogoViewSet(viewsets.ModelViewSet):
    queryset = Catalogo.objects.select_related('veiculo').all()
    serializer_class = CatalogoSerializer


class CatalogoListView(ListView):
    model = Catalogo
    template_name = 'catalogo/lista.html'
    context_object_name = 'catalogos'


class CatalogoDetailView(DetailView):
    model = Catalogo
    template_name = 'catalogo/detalhe.html'
    context_object_name = 'catalogo'


class CatalogoCreateView(CreateView):
    model = Catalogo
    form_class = CatalogoForm
    template_name = 'catalogo/form.html'
    success_url = reverse_lazy('catalogo_web:lista')


class CatalogoUpdateView(UpdateView):
    model = Catalogo
    form_class = CatalogoForm
    template_name = 'catalogo/form.html'
    success_url = reverse_lazy('catalogo_web:lista')


class CatalogoDeleteView(DeleteView):
    model = Catalogo
    template_name = 'catalogo/confirmar_delete.html'
    success_url = reverse_lazy('catalogo_web:lista')
    context_object_name = 'catalogo'