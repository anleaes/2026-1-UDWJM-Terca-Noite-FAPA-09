from rest_framework import viewsets

from .models import Veiculo
from .serializers import VeiculoSerializer


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.select_related('grupo').all().order_by('placa')
    serializer_class = VeiculoSerializer