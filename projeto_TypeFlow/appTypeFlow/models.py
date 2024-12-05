from django.db import models
from django.contrib.auth.models import User
    
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
    descricaoGeral = models.TextField()  # Descrição do tipo MBTI
    classe = models.TextField(max_length=46)
    subclasse = models.TextField(max_length=46, unique=True)
    salaDeAula = models.TextField(default='')
    gruposDeProjetos= models.TextField(default='')
    pessoaFamosa1 = models.ImageField(upload_to='personalities/', null=True, blank=True)
    pessoaFamosa2 = models.ImageField(upload_to='personalities/', null=True, blank=True)
    pessoaFamosa3 = models.ImageField(upload_to='personalities/', null=True, blank=True)
    pessoaFamosa4 = models.ImageField(upload_to='personalities/', null=True, blank=True)
    pessoaFamosa5 = models.ImageField(upload_to='personalities/', null=True, blank=True)
    pessoaFamosa6 = models.ImageField(upload_to='personalities/', null=True, blank=True)
    primary_color = models.CharField(max_length=7, default='#000000')  # Cor principal
    background_color = models.CharField(max_length=7, default='#ffffff')  # Cor de fundo
    sidebar_color = models.CharField(max_length=7, default='#000000') # Cor da sidebar

    def __str__(self):
        return self.type

class Turmas(models.Model):
    CURSO_CHOICES = [
        ('SI', 'Sistemas de Informação'),
        ('CC', 'Ciência da Computação'),
        ('ADS', 'Análise e Desenvolvimento de Sistemas'),
        ('GTI', 'Gestão da Tecnologia da Informação'),
        ('Design', 'Design'),
    ]

    PERIODO_CHOICES = [
        (1, '1º Período'),
        (2, '2º Período'),
        (3, '3º Período'),
        (4, '4º Período'),
        (5, '5º Período'),
        (6, '6º Período'),
        (7, '7º Período'),
        (8, '8º Período'),
        (9, '9º Período'),
        (10, '10º Período'),
    ]

    TURMA_CHOICES = [
        ('A', 'Turma A'),
        ('B', 'Turma B'),
        ('C', 'Turma C'),
    ]

    curso = models.CharField(max_length=100, choices=CURSO_CHOICES)  # Dropdown para turmas
    periodo = models.PositiveSmallIntegerField(choices=PERIODO_CHOICES, default='0')  # Dropdown para períodos
    turma = models.CharField(max_length=100, choices=TURMA_CHOICES, default='X')