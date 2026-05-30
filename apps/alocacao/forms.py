from django import forms
from .models import Alocacao, HistoricoAlocacao


class AlocacaoForm(forms.ModelForm):
    class Meta:
        model = Alocacao
        fields = [
            'solicitacao',
            'data_inicio',
            'data_fim_prevista',
            'km_inicial',
            'observacao',
        ]

        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim_prevista': forms.DateInput(attrs={'type': 'date'}),
            'observacao': forms.Textarea(attrs={'rows': 4}),
        }


class HistoricoAlocacaoForm(forms.ModelForm):
    class Meta:
        model = HistoricoAlocacao
        fields = [
            'alocacao',
            'status_anterior',
            'status_novo',
            'observacao',
            'responsavel_alteracao',
        ]
