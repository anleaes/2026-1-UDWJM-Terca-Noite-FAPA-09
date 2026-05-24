from decimal import Decimal, InvalidOperation

from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils.dateparse import parse_date
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Manutencao
from .serializers import ManutencaoSerializer
from .services import abrir_manutencao, finalizar_manutencao


def _raise_api_validation_error(error):
    messages = error.messages if hasattr(error, 'messages') else [str(error)]
    raise ValidationError({'detail': messages})


class ManutencaoViewSet(viewsets.ModelViewSet):
    queryset = Manutencao.objects.select_related('veiculo').all()
    serializer_class = ManutencaoSerializer

    def perform_create(self, serializer):
        dados = serializer.validated_data
        try:
            serializer.instance = abrir_manutencao(
                veiculo=dados['veiculo'],
                tipo_manutencao=dados['tipo_manutencao'],
                descricao=dados['descricao'],
                data_entrada=dados['data_entrada'],
                custo=dados['custo']
            )
        except DjangoValidationError as error:
            _raise_api_validation_error(error)

    @action(detail=True, methods=['post'])
    def finalizar(self, request, pk=None):
        manutencao = self.get_object()
        data_saida = parse_date(request.data.get('data_saida', ''))
        custo = request.data.get('custo')

        if data_saida is None:
            raise ValidationError({'data_saida': 'Informe uma data valida no formato YYYY-MM-DD.'})

        if custo in (None, ''):
            custo = None
        else:
            try:
                custo = Decimal(str(custo))
            except (InvalidOperation, TypeError, ValueError):
                raise ValidationError({'custo': 'Informe um custo valido.'})

        try:
            manutencao = finalizar_manutencao(
                manutencao=manutencao,
                data_saida=data_saida,
                custo=custo
            )
        except DjangoValidationError as error:
            _raise_api_validation_error(error)

        serializer = self.get_serializer(manutencao)
        return Response(serializer.data, status=status.HTTP_200_OK)
