from django.forms import ModelForm
from .models import Formulario

class Formularioform(ModelForm):
    class Meta:
        model = Formulario
        fields = '__all__'