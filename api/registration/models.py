from django.db import models


# Create your models here.
class Registration(models.Model):
    cpf = models.IntegerField(primary_key=True, editable=False)
    nome = models.CharField(max_length=255)
    dataNascimento = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=70)
    cep = models.IntegerField()
