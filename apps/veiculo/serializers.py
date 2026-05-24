from rest_framework import serializers

from .models import Veiculo


class VeiculoSerializer(serializers.ModelSerializer):
    grupo_nome = serializers.StringRelatedField(source='grupo', read_only=True)

    class Meta:
        model = Veiculo
        fields = [
            'id',
            'grupo',
            'grupo_nome',
            'placa',
            'renavam',
            'marca',
            'modelo',
            'ano_fabricacao',
            'ano_modelo',
            'cor',
            'quilometragem',
            'tipo_combustivel',
            'status',
        ]