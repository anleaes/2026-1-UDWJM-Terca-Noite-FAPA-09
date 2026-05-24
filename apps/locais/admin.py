from django.contrib import admin
from .models import Local


@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'estado', 'cep')
    search_fields = ('nome', 'cidade', 'estado', 'cep')
    list_filter = ('estado', 'cidade')

