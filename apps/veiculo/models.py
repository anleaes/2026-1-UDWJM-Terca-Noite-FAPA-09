from django.db import models
from grupo_veiculo.models import GrupoVeiculo


class Veiculo(models.Model):
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('alocado', 'Alocado'),
        ('manutencao', 'Manutenção'),
        ('inativo', 'Inativo'),
    ]

    TIPO_COMBUSTIVEL_CHOICES = [
        ('gasolina', 'Gasolina'),
        ('etanol', 'Etanol'),
        ('flex', 'Flex'),
        ('diesel', 'Diesel'),
        ('eletrico', 'Elétrico'),
        ('hibrido', 'Híbrido'),
    ]

    grupo = models.ForeignKey(
        GrupoVeiculo,
        on_delete=models.PROTECT,
        related_name='veiculos'
    )

    placa = models.CharField(max_length=10, unique=True)
    renavam = models.CharField(max_length=20, unique=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano_fabricacao = models.IntegerField()
    ano_modelo = models.IntegerField()
    cor = models.CharField(max_length=50)
    quilometragem = models.FloatField()
    tipo_combustivel = models.CharField(
        max_length=20,
        choices=TIPO_COMBUSTIVEL_CHOICES
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='disponivel'
    )

    def __str__(self):
        return f'{self.marca} {self.modelo} - {self.placa}'