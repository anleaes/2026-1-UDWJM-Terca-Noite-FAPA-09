from django.db import models

from django.db import models

from users.models import Cliente, Funcionario
from veiculo.models import Veiculo
from locais.models import Local


class Solicitacao(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovada', 'Aprovada'),
        ('recusada', 'Recusada'),
        ('cancelada', 'Cancelada'),
        ('finalizada', 'Finalizada'),
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='solicitacoes'
    )

    veiculo = models.ForeignKey(
        Veiculo,
        on_delete=models.PROTECT,
        related_name='solicitacoes'
    )

    local = models.ForeignKey(
        Local,
        on_delete=models.PROTECT,
        related_name='solicitacoes'
    )

    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.SET_NULL,
        related_name='solicitacoes_analisadas',
        null=True,
        blank=True
    )

    data_solicitacao = models.DateField(auto_now_add=True)
    data_inicio_desejada = models.DateField()
    data_fim_desejada = models.DateField()
    motivo = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente'
    )
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Solicitação #{self.id} - {self.cliente.nome}'
