from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils.dateparse import parse_date
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Alocacao, HistoricoAlocacao
from .serializers import AlocacaoSerializer, HistoricoAlocacaoSerializer
from .services import cancelar_alocacao, criar_alocacao, finalizar_alocacao

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import AlocacaoForm


def _raise_api_validation_error(error):
    messages = error.messages if hasattr(error, 'messages') else [str(error)]
    raise ValidationError({'detail': messages})


class AlocacaoViewSet(viewsets.ModelViewSet):
    queryset = Alocacao.objects.select_related('solicitacao').all()
    serializer_class = AlocacaoSerializer

    def perform_create(self, serializer):
        dados = serializer.validated_data
        try:
            serializer.instance = criar_alocacao(
                solicitacao=dados['solicitacao'],
                data_inicio=dados['data_inicio'],
                data_fim_prevista=dados['data_fim_prevista'],
                km_inicial=dados['km_inicial'],
                observacao=dados.get('observacao'),
                responsavel_alteracao='API'
            )
        except DjangoValidationError as error:
            _raise_api_validation_error(error)

    @action(detail=True, methods=['post'])
    def finalizar(self, request, pk=None):
        alocacao = self.get_object()
        data_fim_real = parse_date(request.data.get('data_fim_real', ''))
        km_final = request.data.get('km_final')

        if data_fim_real is None:
            raise ValidationError({'data_fim_real': 'Informe uma data valida no formato YYYY-MM-DD.'})

        try:
            km_final = float(km_final)
        except (TypeError, ValueError):
            raise ValidationError({'km_final': 'Informe uma quilometragem final valida.'})

        try:
            alocacao = finalizar_alocacao(
                alocacao=alocacao,
                data_fim_real=data_fim_real,
                km_final=km_final,
                observacao=request.data.get('observacao'),
                responsavel_alteracao=request.data.get('responsavel_alteracao', 'API')
            )
        except DjangoValidationError as error:
            _raise_api_validation_error(error)

        serializer = self.get_serializer(alocacao)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def cancelar(self, request, pk=None):
        try:
            alocacao = cancelar_alocacao(
                alocacao=self.get_object(),
                observacao=request.data.get('observacao'),
                responsavel_alteracao=request.data.get('responsavel_alteracao', 'API')
            )
        except DjangoValidationError as error:
            _raise_api_validation_error(error)

        serializer = self.get_serializer(alocacao)
        return Response(serializer.data, status=status.HTTP_200_OK)


class HistoricoAlocacaoViewSet(viewsets.ModelViewSet):
    queryset = HistoricoAlocacao.objects.select_related('alocacao').all()
    serializer_class = HistoricoAlocacaoSerializer


class AlocacaoListView(ListView):
    model = Alocacao
    template_name = 'alocacao/lista.html'
    context_object_name = 'alocacoes'

class AlocacaoDetailView(DetailView):
    model = Alocacao
    template_name = 'alocacao/detalhe.html'
    context_object_name = 'alocacao'


class AlocacaoCreateView(CreateView):
    model = Alocacao
    form_class = AlocacaoForm
    template_name = 'alocacao/form.html'
    success_url = reverse_lazy('alocacao_web:lista')


class AlocacaoUpdateView(UpdateView):
    model = Alocacao
    form_class = AlocacaoForm
    template_name = 'alocacao/form.html'
    success_url = reverse_lazy('alocacao_web:lista')


class AlocacaoDeleteView(DeleteView):
    model = Alocacao
    template_name = 'alocacao/confirmar_delete.html'
    success_url = reverse_lazy('alocacao_web:lista')


class HistoricoAlocacaoListView(ListView):
    model = HistoricoAlocacao
    template_name = 'alocacao/historicos.html'
    context_object_name = 'historicos'
