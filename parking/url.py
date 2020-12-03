from django.urls import path, include
from .views import (
    index, serviços, sobre, planos,
    contatos
    )


urlpatterns = [
    path('index/', index, name='parking_index'),
    path('serviços/', serviços, name='parking_serviço'),
    path('sobre/', sobre, name='parking_sobre'),
    path('planos/', planos, name='parking_planos'),
    path('contatos/', contatos, name='parking_contato'),
]