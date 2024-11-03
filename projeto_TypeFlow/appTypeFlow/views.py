from django.shortcuts import render, redirect
from .forms import QuizForm
from .models import Question

def calculate_mbti(answers):
    scores = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}
    for question_id, choice in answers.items():
        question = Question.objects.get(id=question_id.split('_')[-1])
        if question.dimension == 'EI':
            scores[choice] += 1

    mbti_type = (
        ('E' if scores['E'] > scores['I'] else 'I') +
        ('S' if scores['S'] > scores['N'] else 'N') +
        ('T' if scores['T'] > scores['F'] else 'F') +
        ('J' if scores['J'] > scores['P'] else 'P')
    )
    return mbti_type

def quiz_view(request, page=1):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            answers = request.session.get('quiz_answers', {})
            for key, value in form.cleaned_data.items():
                answers[key] = value
            request.session['quiz_answers'] = answers
            
            if page < 4:
                return redirect('quiz_view', page=page+1)
            else:
                mbti_type = calculate_mbti(answers)
                request.session['mbti_type'] = mbti_type
                
                # Salvar o resultado no banco de dados
                MBTIResult.objects.create(
                    user=request.user,
                    mbti_type=mbti_type
                )

                return redirect('result_view')
    else:
        form = QuizForm()

    total_questions = len(form.fields)
    return render(request, f'testes/teste{page}_mbti.html', {'form': form, 'total_questions': total_questions})

def result_view(request):
    mbti_type = request.session.get('mbti_type')  # Obter o tipo MBTI da sessão

    # Se o usuário já fez o teste, busca o resultado no banco de dados
    result = MBTIResult.objects.filter(user=request.user).latest('date_taken')

    return render(request, 'testes/result.html', {'mbti_type': mbti_type, 'result': result})

# Outras views
def home_aluno(request):
    return render(request, 'aluno/home_aluno.html')

def teste1_mbti(request):
    return render(request, 'testes/teste1_mbti.html')

def teste2_mbti(request):
    return render(request, 'testes/teste2_mbti.html')

def teste3_mbti(request):
    return render(request, 'testes/teste3_mbti.html')
