from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import Formularioform


# Create your views here.

def index(request):
    return render(request, 'parking/index.html')


def serviços(request):
    return render(request, 'parking/serviços.html')


def sobre(request):
    return render(request, 'parking/sobre.html')


def planos(request):
    return render(request, 'parking/planos.html')


def form_contato(request):
    form = Formularioform(request.POST or None)

    if not form.is_valid():
        form.save()
        return redirect('parking_confirm')
    
    else:
        form = Formularioform(request.POST)
        return render(request, 'parking/contatos.html', {'form': form})

    

def contatos(request):
    data = {}
    form = Formularioform(request.POST or None)
    data['form'] = form

    return render(request, 'parking/contatos.html', data)


def obrigado(request):
    return render(request, 'parking/thankyou.html')
