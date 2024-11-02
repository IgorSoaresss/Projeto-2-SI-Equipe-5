from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def teste_personalidade(request):
    # Dados e lógica para o teste de personalidade
    return render(request, 'teste/teste_personalidade.html')

def home_aluno(request):
    return render(request, 'aluno/home_aluno.html')

def teste_personalidade(request):
    return render(request, 'testes/teste_personalidade.html')

def teste2_mbti(request):
    return render(request, 'testes/teste2_mbti.html')