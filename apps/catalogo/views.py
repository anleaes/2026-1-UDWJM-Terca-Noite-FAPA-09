from rest_framework import viewsets

from .models import Catalogo
from .serializers import CatalogoSerializer


class CatalogoViewSet(viewsets.ModelViewSet):
    queryset = Catalogo.objects.select_related('veiculo').all()
    serializer_class = CatalogoSerializer