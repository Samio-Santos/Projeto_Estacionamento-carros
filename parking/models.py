from django.db import models

# Create your models here.

class Formulario(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=40, blank=False, null=False)
    telefone = models.CharField(max_length=30, blank=False, null=False)
    mensagem = models.TextField()
    respondido = models.BooleanField(default=False, blank=True, null=True)


    def __str__(self):
        return self.nome
