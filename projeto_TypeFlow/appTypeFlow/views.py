from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def base(request):
    return render(request, 'base.html')

def teste_personalidade(request):
    # Dados e lógica para o teste de personalidade
    return render(request, 'teste/teste_personalidade.html')

def home_aluno(request):
    return render(request, 'aluno/home.html')