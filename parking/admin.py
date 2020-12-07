from django.contrib import admin
from .models import Formulario

# Register your models here.

class Formularioadmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'mensagem')
    search_fields = ('nome', 'email')
    # ordering = ('order',)


admin.site.register(Formulario, Formularioadmin)