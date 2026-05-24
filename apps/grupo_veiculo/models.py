from django.db import models


class GrupoVeiculo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    capacidade_passageiros = models.IntegerField()
    tipo_combustivel = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome