from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def base(request):
    return render(request, 'base.html')

@login_required
def home_aluno(request):
    # buscar dados relacionados ao aluno, como progresso, testes realizados...
    context = {
        'nome_aluno': request.user.first_name,  
    }
    return render(request, 'aluno/home.html', context)