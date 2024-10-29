
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teste_mbti/', views.teste_mbti, name='teste_mbti'),
    path('calcular_mbti/', views.calcular_mbti, name='calcular_mbti'),  # New route for MBTI calculation
]
