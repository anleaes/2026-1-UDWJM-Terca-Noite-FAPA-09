from rest_framework import serializers

from .models import Alocacao, HistoricoAlocacao


class HistoricoAlocacaoSerializer(serializers.ModelSerializer):
    alocacao_descricao = serializers.StringRelatedField(source='alocacao', read_only=True)

    class Meta:
        model = HistoricoAlocacao
        fields = [
            'id',
            'alocacao',
            'alocacao_descricao',
            'data_registro',
            'status_anterior',
            'status_novo',
            'observacao',
            'responsavel_alteracao',
        ]


class AlocacaoSerializer(serializers.ModelSerializer):
    solicitacao_descricao = serializers.StringRelatedField(source='solicitacao', read_only=True)

    class Meta:
        model = Alocacao
        fields = [
            'id',
            'solicitacao',
            'solicitacao_descricao',
            'data_inicio',
            'data_fim_prevista',
            'data_fim_real',
            'km_inicial',
            'km_final',
            'status',
            'observacao',
        ]
