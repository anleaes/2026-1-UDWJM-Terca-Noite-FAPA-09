from django import forms
from .models import GrupoVeiculo


class GrupoVeiculoForm(forms.ModelForm):
    class Meta:
        model = GrupoVeiculo
        fields = '__all__'