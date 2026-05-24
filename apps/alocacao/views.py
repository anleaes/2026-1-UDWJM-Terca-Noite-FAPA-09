from rest_framework import viewsets

from .models import Alocacao, HistoricoAlocacao
from .serializers import AlocacaoSerializer, HistoricoAlocacaoSerializer


class AlocacaoViewSet(viewsets.ModelViewSet):
    queryset = Alocacao.objects.select_related('solicitacao').all()
    serializer_class = AlocacaoSerializer


class HistoricoAlocacaoViewSet(viewsets.ModelViewSet):
    queryset = HistoricoAlocacao.objects.select_related('alocacao').all()
    serializer_class = HistoricoAlocacaoSerializer
