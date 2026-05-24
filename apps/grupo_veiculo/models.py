from django.db import models


class GrupoVeiculo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    capacidade_passageiros = models.IntegerField()
    valor_base_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome