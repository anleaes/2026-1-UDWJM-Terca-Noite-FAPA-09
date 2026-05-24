from rest_framework import viewsets

from .models import GrupoVeiculo
from .serializers import GrupoVeiculoSerializer


class GrupoVeiculoViewSet(viewsets.ModelViewSet):
    queryset = GrupoVeiculo.objects.all().order_by('nome')
    serializer_class = GrupoVeiculoSerializer