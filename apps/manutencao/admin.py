from django.contrib import admin

from .models import Manutencao, Peca, PecaManutencao


admin.site.register(Manutencao)
admin.site.register(Peca)
admin.site.register(PecaManutencao)
