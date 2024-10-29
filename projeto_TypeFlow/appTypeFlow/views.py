from django.shortcuts import render
from django.http import HttpResponse

from .forms import QuizForm
from .models import Question

def index(request):
    return HttpResponse("Olá, este é o TypeFlow!")

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

def quiz_view(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            answers = {key: form.cleaned_data[key] for key in form.cleaned_data}
            mbti_type = calculate_mbti(answers)
            return render(request, 'result.html', {'mbti_type': mbti_type})
    else:
        form = QuizForm()
    return render(request, 'quiz.html', {'form': form})
