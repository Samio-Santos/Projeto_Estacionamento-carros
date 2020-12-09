from django.contrib import admin
from .models import Formulario

# Register your models here.

class Formularioadmin(admin.ModelAdmin):
    list_display = ('id', 'respondido', 'nome', 'email', 'telefone', 'mensagem')
    search_fields = ('nome', 'email')
    list_display_links = ('id', 'nome')
    list_per_page = 10
    # ordering = ('order',)


admin.site.register(Formulario, Formularioadmin)