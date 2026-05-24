from django import forms
from .models import GrupoVeiculo


class GrupoVeiculoForm(forms.ModelForm):
    class Meta:
        model = GrupoVeiculo
        fields = [
            'nome',
            'descricao',
            'capacidade_passageiros',
            'valor_base_diaria',
            'ativo',
        ]
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'capacidade_passageiros': 'Capacidade de passageiros',
            'valor_base_diaria': 'Valor base da diária (R$)',
        }