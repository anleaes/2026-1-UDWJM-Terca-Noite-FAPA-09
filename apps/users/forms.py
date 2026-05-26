from django import forms
from .models import Cliente, Funcionario


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome',
            'email',
            'senha',
            'cpf',
            'telefone',
            'status',
            'cnh',
            'categoria_cnh',
            'validade_cnh',
        ]

        widgets = {
            'validade_cnh': forms.DateInput(attrs={'type': 'date'}),
            'senha': forms.PasswordInput(),
        }


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            'nome',
            'email',
            'senha',
            'cpf',
            'telefone',
            'status',
            'nivel_acesso',
            'cargo',
            'ativo',
        ]

        widgets = {
            'senha': forms.PasswordInput(),
        }