from django.urls import path
from . import views  # Referencia as views do próprio app

urlpatterns = [
    path('', views.home_aluno, name='home_aluno'),
    path('teste_personalidade/', views.teste_personalidade, name='teste_personalidade'),
    path('teste2_mbti/', views.teste2_mbti, name='teste2_mbti'),
    path('teste3_mbti/', views.teste3_mbti, name='teste3_mbti'),
    path('save_response/', views.save_mbti_response, name='save_response'),
    
    ]
