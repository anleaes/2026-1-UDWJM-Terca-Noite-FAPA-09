from django import forms

from .models import Manutencao


class ManutencaoForm(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = [
            'veiculo',
            'tipo_manutencao',
            'descricao',
            'data_entrada',
            'custo',
        ]
        widgets = {
            'data_entrada': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }
