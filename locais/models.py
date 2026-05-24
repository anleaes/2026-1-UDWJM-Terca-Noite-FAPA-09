from django.db import models


class Local(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.nome} - {self.cidade}/{self.estado}'