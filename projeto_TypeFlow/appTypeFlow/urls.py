from django.urls import path
from . import views  # Referencia as views do próprio app

urlpatterns = [
    path('', views.home_aluno, name='home_aluno'),
    path('professor/home/', views.home_professor, name='home_professor'),
    path('professor/turmas/', views.professor_turmas, name='professor_turmas'),
    path('professor/turmas/cadastro', views.turmas_cadastro, name='turmas_cadastro'),
    path('teste1_mbti/', views.teste1_mbti, name='teste1_mbti'),
    path('teste2_mbti/', views.teste2_mbti, name='teste2_mbti'),
    path('teste3_mbti/', views.teste3_mbti, name='teste3_mbti'),
    path('teste4_mbti/', views.teste4_mbti, name='teste4_mbti'),
    path('quiz/<int:page>/', views.quiz_view, name='quiz_view'),
    path('result/', views.result_view, name='result_view'),
    ]
