from django.db import models
from veiculo.models import Veiculo


class Catalogo(models.Model):
    veiculo = models.OneToOneField(
        Veiculo,
        on_delete=models.PROTECT,
        related_name='catalogo'
    )

    preco_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='catalogo_veiculos/', blank=True, null=True)
    descricao_comercial = models.TextField()
    destaque = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'Catálogo - {self.veiculo}'