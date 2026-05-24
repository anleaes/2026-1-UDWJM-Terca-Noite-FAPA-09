from rest_framework import viewsets

from .models import Manutencao
from .serializers import ManutencaoSerializer


class ManutencaoViewSet(viewsets.ModelViewSet):
    queryset = Manutencao.objects.select_related('veiculo').all()
    serializer_class = ManutencaoSerializer
