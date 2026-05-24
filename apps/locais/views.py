from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets

from .forms import LocalForm
from .models import Local
from .serializers import LocalSerializer


class LocalListView(ListView):
    model = Local
    template_name = 'locais/lista.html'
    context_object_name = 'locais'


class LocalDetailView(DetailView):
    model = Local
    template_name = 'locais/detalhe.html'
    context_object_name = 'local'


class LocalCreateView(CreateView):
    model = Local
    form_class = LocalForm
    template_name = 'locais/form.html'
    success_url = reverse_lazy('locais:lista')


class LocalUpdateView(UpdateView):
    model = Local
    form_class = LocalForm
    template_name = 'locais/form.html'
    success_url = reverse_lazy('locais:lista')


class LocalDeleteView(DeleteView):
    model = Local
    template_name = 'locais/confirmar_delete.html'
    success_url = reverse_lazy('locais:lista')


class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
