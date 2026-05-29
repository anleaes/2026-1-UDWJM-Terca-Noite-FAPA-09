from django.db import models


class Pessoa(models.Model):
    status_escolhas = [
        ('ATIVO', 'Ativo'),
        ('INATIVO', 'Inativo'),
    ]
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)
    status = models.CharField(
        max_length=10,
        choices=status_escolhas,
        default='ATIVO'
    )

    class Meta:
        abstract = True


class Cliente(Pessoa):
    cnh = models.CharField(max_length=20)
    categoria_cnh = models.CharField(max_length=5)
    validade_cnh = models.DateField()
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Funcionario(Pessoa):
    nivel_acesso = models.CharField(max_length=50)
    cargo = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
