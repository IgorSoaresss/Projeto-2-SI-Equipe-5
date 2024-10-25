from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Exemplo de rota associando a view 'home'
    path('teste-mbti/', views.teste_mbti, name='teste_mbti'),
]