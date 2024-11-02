from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
    
class Question(models.Model):
    text = models.CharField(max_length=255)
    dimension = models.CharField(max_length=2, choices=[
        ('EI', 'Extroversion/Introversion'),
        ('SN', 'Sensing/Intuition'),
        ('TF', 'Thinking/Feeling'),
        ('JP', 'Judging/Perceiving')
    ])

class MBTIResponse(models.Model):
    user_id = models.IntegerField()  # Para associar a resposta ao usuário, ajuste conforme necessário
    response_data = models.TextField()  # Armazena respostas como uma string simples
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Response from user {self.user_id}'
