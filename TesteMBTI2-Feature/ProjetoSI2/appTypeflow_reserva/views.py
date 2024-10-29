
from django.shortcuts import render
from django.http import HttpResponse

# Home view
def home(request):
    return render(request, 'appTypeflow_reserva/home.html')

# View to render MBTI test page
def teste_mbti(request):
    return render(request, 'appTypeflow_reserva/teste_mbti.html')

# Function to calculate MBTI based on simplified scoring
def calcular_mbti(request):
    if request.method == 'POST':
        # Initialize trait scores
        pontuacao = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}
        
        # Define responses for each question, using 'nao' as default to avoid missing keys
        respostas = {
            'E_I': request.POST.get('E_I', 'nao'),  # Extroversion vs Introversion
            'S_N': request.POST.get('S_N', 'nao'),  # Sensing vs Intuition
            'T_F': request.POST.get('T_F', 'nao'),  # Thinking vs Feeling
            'J_P': request.POST.get('J_P', 'nao')   # Judging vs Perceiving
        }
        
        # Process each response safely, incrementing for "Sim" and "Não" based on expected choice
        for key, response in respostas.items():
            first_trait, second_trait = key.split('_')
            if response.lower() == 'sim':
                pontuacao[first_trait] += 1
            else:
                pontuacao[second_trait] += 1
        
        # Determine MBTI type based on the scores for each pair
        tipo_mbti = ''
        tipo_mbti += 'E' if pontuacao['E'] >= pontuacao['I'] else 'I'
        tipo_mbti += 'S' if pontuacao['S'] >= pontuacao['N'] else 'N'
        tipo_mbti += 'T' if pontuacao['T'] >= pontuacao['F'] else 'F'
        tipo_mbti += 'J' if pontuacao['J'] >= pontuacao['P'] else 'P'
        
        # Render result
        return render(request, 'appTypeflow_reserva/teste_mbti.html', {'resultado': tipo_mbti})
    
    # Render form if GET request
    return render(request, 'appTypeflow_reserva/teste_mbti.html')
