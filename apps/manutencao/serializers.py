from rest_framework import serializers

from .models import Manutencao, Peca, PecaManutencao


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


class PecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peca
        fields = [
            'id',
            'tipo_peca',
            'fabricante',
            'preco_unitario',
        ]


class PecaManutencaoSerializer(serializers.ModelSerializer):
    manutencao_descricao = serializers.StringRelatedField(source='manutencao', read_only=True)
    peca_descricao = serializers.StringRelatedField(source='peca', read_only=True)

    class Meta:
        model = PecaManutencao
        fields = [
            'id',
            'manutencao',
            'manutencao_descricao',
            'peca',
            'peca_descricao',
            'quantidade',
            'preco_unitario',
            'sub_total',
        ]
