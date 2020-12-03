from django.urls import path, include
from .views import index, serviços

urlpatterns = [
    path('index/', index, name='parking_index'),
    path('serviços/', serviços, name='parking_serviço'),


]