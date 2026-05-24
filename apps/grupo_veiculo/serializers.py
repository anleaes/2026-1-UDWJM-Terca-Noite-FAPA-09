from rest_framework import serializers

from .models import GrupoVeiculo


class GrupoVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoVeiculo
        fields = [
            'id',
            'nome',
            'descricao',
            'capacidade_passageiros',
            'valor_base_diaria',
            'ativo',
        ]