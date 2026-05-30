from django import forms

from .models import Solicitacao


class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = [
            'cliente',
            'veiculo',
            'local',
            'funcionario',
            'data_inicio_desejada',
            'data_fim_desejada',
            'motivo',
            'status',
            'observacao',
        ]
        widgets = {
            'data_inicio_desejada': forms.DateInput(attrs={'type': 'date'}),
            'data_fim_desejada': forms.DateInput(attrs={'type': 'date'}),
            'observacao': forms.Textarea(attrs={'rows': 4}),
        }
