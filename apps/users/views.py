from rest_framework import viewsets
from .models import Cliente, Funcionario
from .serializers import ClienteSerializer, FuncionarioSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('nome')
    serializer_class = ClienteSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all().order_by('nome')
    serializer_class = FuncionarioSerializer