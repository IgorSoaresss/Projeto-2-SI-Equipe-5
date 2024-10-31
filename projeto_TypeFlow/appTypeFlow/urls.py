from django.urls import path
from . import views  # Referencia as views do próprio app

urlpatterns = [
    path('home/', views.home_aluno, name='home_aluno'),]