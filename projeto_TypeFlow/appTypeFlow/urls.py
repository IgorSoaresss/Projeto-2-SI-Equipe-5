from django.urls import path
from . import views  # Referencia as views do próprio app

urlpatterns = [
    path('', views.home_aluno, name='home_aluno'),
    path('teste1_mbti/', views.teste1_mbti, name='teste1_mbti'),
    path('teste2_mbti/', views.teste2_mbti, name='teste2_mbti'),
    path('teste3_mbti/', views.teste3_mbti, name='teste3_mbti')

    ]
