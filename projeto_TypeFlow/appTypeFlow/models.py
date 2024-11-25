from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
    
<<<<<<< HEAD
class Question(models.Model):
    text = models.CharField(max_length=255)
    dimension = models.CharField(max_length=2, choices=[
        ('EI', 'Extroversion/Introversion'),
        ('SN', 'Sensing/Intuition'),
        ('TF', 'Thinking/Feeling'),
        ('JP', 'Judging/Perceiving'),
    ])
=======
class Pergunta(models.Model):
    texto = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50)
>>>>>>> feature-login


    def __str__(self):
        return self.texto

class resposta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = models.CharField(max_length=1) 

    def __str__(self):
        return f"{self.usuario} - {self.pergunta}: {self.resposta}"

class resultadoMBTI(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    mbti_tipo = models.CharField(max_length=4)
    mbti_simplificado = models.CharField(max_length=2)
    perfil = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.usuario} - {self.pergunta} ({self.resposta})"