from django.urls import path
from . import views  # Referencia as views do próprio app

urlpatterns = [
<<<<<<< HEAD
    path('quiz/', views.quiz_view, name='quiz'),
]
=======
    path('', views.home_aluno, name='home_aluno'),
    path('teste_personalidade/', views.teste_personalidade, name='teste_personalidade'),
    path('teste2_mbti/', views.teste2_mbti, name='teste2_mbti'),
    path('teste3_mbti/', views.teste3_mbti, name='teste3_mbti')

    ]
>>>>>>> origin/feature_teste
