from django.db import models
from django.contrib.auth.models import User
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
        ('JP', 'Judging/Perceiving'),
    ])

class MBTIResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mbti_type = models.CharField(max_length=4)  # Armazena o tipo MBTI (ex: 'INTJ', 'ENFP')
    date_taken = models.DateTimeField(auto_now_add=True)  # Armazena a data do teste

    def __str__(self):
        return f"{self.user.username} - {self.mbti_type} ({self.date_taken})"
    
class MBTIDescription(models.Model):
    type = models.CharField(max_length=4, unique=True)  # Ex: "INTJ", "ENFP"
    description = models.TextField()  # Descrição do tipo MBTI
    famous_person_image = models.ImageField(upload_to='personalities/', null=True, blank=True)
    primary_color = models.CharField(max_length=7, default='#000000')  # Cor principal (ex: #1a1aff)
    background_color = models.CharField(max_length=7, default='#ffffff')  # Cor de fundo

    def __str__(self):
        return self.type