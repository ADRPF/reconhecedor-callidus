from django.db import models

# Create your models here.

class Gerente(models.Model):
    login = models.CharField(max_lenght=50)
    senha = models.CharField(max_lenght=50)
    nome_geren = models.CharField(max_lenght=50)
    nível_acesso = models.IntegerField()
    foto_geren = models.ImageField()


    def __str__(self):
        return self.nome_geren
    

class Funcionario(models.Model):
    nome_func = models.CharField(max_lenght=50)
    cargo_func = models.CharField(max_length=50)
    nível_acesso = models.IntegerField()
    foto_func = models.ImageField()
    gerente_Id = models.ForeignKey(Gerente)

    def __str__(self):
        return self.nome_func
    

class Ambiente(models.Model):
    nome_amb = models.CharField(max_length=50)
    nivel_exigido = models.IntegerField()

    def __str__(self):
        return self.nome_amb
    

class Acesso(models.Model):
    id_func = models.ForeignKey(Funcionario)
    id_amb = models.ForeignKey(Ambiente)
    data_acesso = models.DateTimeField()
    resultado = models.BooleanField(default=False)
