from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'parking/index.html')


def serviços(request):
    return render(request, 'parking/serviços.html')


def sobre(request):
    return render(request, 'parking/sobre.html')


def planos(request):
    return render(request, 'parking/planos.html')


def contatos(request):
    return render(request, 'parking/contatos.html')