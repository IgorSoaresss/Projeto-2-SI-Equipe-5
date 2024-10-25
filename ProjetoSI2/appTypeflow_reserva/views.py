from django.shortcuts import render

def home(request):
    return render(request, 'appTypeflow_reserva/home.html')

def teste_mbti(request):
    return render(request, 'appTypeflow_reserva/teste_mbti.html')
