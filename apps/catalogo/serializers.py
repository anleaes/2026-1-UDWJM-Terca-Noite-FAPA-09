from rest_framework import serializers

from .models import Catalogo


class CatalogoSerializer(serializers.ModelSerializer):
    veiculo_descricao = serializers.StringRelatedField(source='veiculo', read_only=True)

    class Meta:
        model = Catalogo
        fields = [
            'id',
            'veiculo',
            'veiculo_descricao',
            'preco_diaria',
            'foto',
            'descricao_comercial',
            'destaque',
            'ativo',
        ]