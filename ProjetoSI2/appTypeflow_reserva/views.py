from django.shortcuts import render

def home(request):
    return render(request, 'appTypeflow_reserva/home.html')
