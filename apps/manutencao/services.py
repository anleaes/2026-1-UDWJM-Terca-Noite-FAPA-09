from django.core.exceptions import ValidationError
from django.db import transaction

from .models import Manutencao


@transaction.atomic
def abrir_manutencao(
    veiculo,
    tipo_manutencao,
    descricao,
    data_entrada,
    custo
):
    if veiculo.status == 'alocado':
        raise ValidationError('Veiculos alocados nao podem entrar em manutencao.')

    if veiculo.status == 'manutencao':
        raise ValidationError('Este veiculo ja esta em manutencao.')

    if veiculo.status == 'inativo':
        raise ValidationError('Veiculos inativos nao podem entrar em manutencao.')

    if custo < 0:
        raise ValidationError('O custo nao pode ser negativo.')

    manutencao = Manutencao.objects.create(
        veiculo=veiculo,
        tipo_manutencao=tipo_manutencao,
        descricao=descricao,
        data_entrada=data_entrada,
        custo=custo,
        status='ABERTA'
    )

    veiculo.status = 'manutencao'
    veiculo.save(update_fields=['status'])

    return manutencao


@transaction.atomic
def finalizar_manutencao(manutencao, data_saida, custo=None):
    if manutencao.status == 'CONCLUIDA':
        raise ValidationError('Esta manutencao ja esta concluida.')

    if manutencao.status == 'CANCELADA':
        raise ValidationError('Manutencoes canceladas nao podem ser finalizadas.')

    if data_saida < manutencao.data_entrada:
        raise ValidationError('A data de saida nao pode ser anterior a data de entrada.')

    manutencao.data_saida = data_saida
    manutencao.status = 'CONCLUIDA'
    update_fields = ['data_saida', 'status']

    if custo is not None:
        if custo < 0:
            raise ValidationError('O custo nao pode ser negativo.')
        manutencao.custo = custo
        update_fields.append('custo')

    manutencao.save(update_fields=update_fields)

    veiculo = manutencao.veiculo
    veiculo.status = 'disponivel'
    veiculo.save(update_fields=['status'])

    return manutencao


@transaction.atomic
def cancelar_manutencao(manutencao):
    if manutencao.status == 'CONCLUIDA':
        raise ValidationError('Manutencoes concluidas nao podem ser canceladas.')

    if manutencao.status == 'CANCELADA':
        raise ValidationError('Esta manutencao ja esta cancelada.')

    manutencao.status = 'CANCELADA'
    manutencao.save(update_fields=['status'])

    veiculo = manutencao.veiculo
    veiculo.status = 'disponivel'
    veiculo.save(update_fields=['status'])

    return manutencao
