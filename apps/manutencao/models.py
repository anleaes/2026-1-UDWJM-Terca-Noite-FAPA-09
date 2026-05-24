from django.db import models


class Manutencao(models.Model):
    STATUS_CHOICES = [
        ('ABERTA', 'Aberta'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('CONCLUIDA', 'Concluida'),
        ('CANCELADA', 'Cancelada'),
    ]

    veiculo = models.ForeignKey(
        'veiculo.Veiculo',
        on_delete=models.PROTECT,
        related_name='manutencoes'
    )
    tipo_manutencao = models.CharField(max_length=100)
    descricao = models.TextField()
    data_entrada = models.DateField()
    data_saida = models.DateField(null=True, blank=True)
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ABERTA'
    )

    def __str__(self):
        return f'{self.tipo_manutencao} - {self.veiculo}'
