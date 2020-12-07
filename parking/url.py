from django.urls import path, include
from .views import (
    index, serviços, sobre, planos,
    contatos, form_contato, obrigado
    )


urlpatterns = [
    path('index/', index, name='parking_index'),
    path('serviços/', serviços, name='parking_serviço'),
    path('sobre/', sobre, name='parking_sobre'),
    path('planos/', planos, name='parking_planos'),
    path('contatos/', contatos, name='parking_contato'),
    path('contatos-form/', form_contato, name='parking_contatoForm'),
    path('confirm-form/', obrigado, name='parking_confirm'),

]