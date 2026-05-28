from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets

from .forms import ClienteForm, FuncionarioForm
from .models import Cliente, Funcionario
from .serializers import ClienteSerializer, FuncionarioSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('nome')
    serializer_class = ClienteSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all().order_by('nome')
    serializer_class = FuncionarioSerializer


class ClienteListView(ListView):
    model = Cliente
    template_name = 'users/clientes/lista.html'
    context_object_name = 'clientes'


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'users/clientes/detalhe.html'
    context_object_name = 'cliente'


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'users/clientes/form.html'
    success_url = reverse_lazy('users_web:clientes_lista')


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'users/clientes/form.html'
    success_url = reverse_lazy('users_web:clientes_lista')


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'users/clientes/confirmar_delete.html'
    success_url = reverse_lazy('users_web:clientes_lista')


class FuncionarioListView(ListView):
    model = Funcionario
    template_name = 'users/funcionarios/lista.html'
    context_object_name = 'funcionarios'


class FuncionarioDetailView(DetailView):
    model = Funcionario
    template_name = 'users/funcionarios/detalhe.html'
    context_object_name = 'funcionario'


class FuncionarioCreateView(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'users/funcionarios/form.html'
    success_url = reverse_lazy('users_web:funcionarios_lista')


class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'users/funcionarios/form.html'
    success_url = reverse_lazy('users_web:funcionarios_lista')


class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = 'users/funcionarios/confirmar_delete.html'
    success_url = reverse_lazy('users_web:funcionarios_lista')