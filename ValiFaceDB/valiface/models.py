from django.db import models

# Create your models here.

class Agente(models.Model):
    login = models.EmailField()
    senha = models.CharField(max_length=50)
    nome_agent = models.CharField(max_length=50)
    permissao_agent = models.IntegerField()
    foto_agent = models.ImageField()

    def __str__(self):
        return self.nome_agent
    

class Funcionario(models.Model):
    nome_func = models.CharField(max_length=50)
    cargo_func = models.CharField(max_length=50)
    foto_func = models.ImageField()

    def __str__(self):
        return self.nome_func
    

class Cadastro(models.Model):
    supervisor_cad = models.ForeignKey(Agente, on_delete=models.DO_NOTHING)
    func_cad = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)
    data_cad = models.DateTimeField()
    

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    cor = models.CharField(max_length=7)

    def __str__(self):
        return self.nome
 

class Licenca(models.Model):
    func_id = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data_ini = models.DateField()
    data_fim = models.DateField()


class Setor(models.Model):
    nome_amb = models.CharField(max_length=50)
    nivel_exigido = models.IntegerField()

    def __str__(self):
        return self.nome_amb
    
class Resultado(models.Model):
    tipo_resultado = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_resultado

class Acesso(models.Model):
    id_func = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    id_setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    id_resultado = models.OneToOneField(Resultado, on_delete=models.CASCADE)
    data_acesso = models.DateTimeField()
