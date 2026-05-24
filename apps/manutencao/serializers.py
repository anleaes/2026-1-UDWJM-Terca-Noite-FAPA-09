from rest_framework import serializers

from .models import Manutencao


class ManutencaoSerializer(serializers.ModelSerializer):
    veiculo_descricao = serializers.StringRelatedField(source='veiculo', read_only=True)

    class Meta:
        model = Manutencao
        fields = [
            'id',
            'veiculo',
            'veiculo_descricao',
            'tipo_manutencao',
            'descricao',
            'data_entrada',
            'data_saida',
            'custo',
            'status',
        ]
