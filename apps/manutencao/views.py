from decimal import Decimal, InvalidOperation

from django.core.exceptions import ValidationError as DjangoValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.dateparse import parse_date
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .forms import ManutencaoForm
from .models import Manutencao, Peca, PecaManutencao
from .serializers import ManutencaoSerializer, PecaManutencaoSerializer, PecaSerializer
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


class PecaViewSet(viewsets.ModelViewSet):
    queryset = Peca.objects.all().order_by('tipo_peca', 'fabricante')
    serializer_class = PecaSerializer


class PecaManutencaoViewSet(viewsets.ModelViewSet):
    queryset = PecaManutencao.objects.select_related(
        'manutencao',
        'peca'
    ).all()
    serializer_class = PecaManutencaoSerializer


class ManutencaoListView(ListView):
    model = Manutencao
    template_name = 'manutencao/lista.html'
    context_object_name = 'manutencoes'
    queryset = Manutencao.objects.select_related('veiculo').all().order_by('-data_entrada')


class ManutencaoDetailView(DetailView):
    model = Manutencao
    template_name = 'manutencao/detalhe.html'
    context_object_name = 'manutencao'


class ManutencaoCreateView(CreateView):
    model = Manutencao
    form_class = ManutencaoForm
    template_name = 'manutencao/form.html'
    success_url = reverse_lazy('manutencao_web:lista')

    def form_valid(self, form):
        try:
            abrir_manutencao(
                veiculo=form.cleaned_data['veiculo'],
                tipo_manutencao=form.cleaned_data['tipo_manutencao'],
                descricao=form.cleaned_data['descricao'],
                data_entrada=form.cleaned_data['data_entrada'],
                custo=form.cleaned_data['custo']
            )
        except DjangoValidationError as error:
            form.add_error(None, error)
            return self.form_invalid(form)

        return HttpResponseRedirect(self.get_success_url())


class ManutencaoUpdateView(UpdateView):
    model = Manutencao
    form_class = ManutencaoForm
    template_name = 'manutencao/form.html'
    success_url = reverse_lazy('manutencao_web:lista')


class ManutencaoDeleteView(DeleteView):
    model = Manutencao
    template_name = 'manutencao/confirmar_delete.html'
    context_object_name = 'manutencao'
    success_url = reverse_lazy('manutencao_web:lista')
