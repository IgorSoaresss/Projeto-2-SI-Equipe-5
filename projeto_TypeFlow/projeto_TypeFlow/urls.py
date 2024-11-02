from django.contrib import admin
from django.urls import path, include
from appTypeFlow import views  # Certifique-se de que o app é appTypeFlow (ou ajuste conforme necessário)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appTypeFlow/', include('appTypeFlow.urls')),  # Inclui URLs do app appTypeFlow,  
    path('teste_personalidade/', views.teste_personalidade, name='teste_personalidade'),  # URL para teste de personalidade
    path('', views.home_aluno, name='home_aluno'),  # Define a home_aluno como a página inicia
]
