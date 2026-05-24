from django.contrib import admin

from django.contrib import admin
from .models import Solicitacao


@admin.register(Solicitacao)
class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cliente',
        'veiculo',
        'local',
        'status',
        'data_inicio_desejada',
        'data_fim_desejada',
    )
    search_fields = (
        'cliente__nome',
        'veiculo__placa',
        'veiculo__modelo',
        'local__nome',
        'status',
    )
    list_filter = ('status', 'data_solicitacao')
