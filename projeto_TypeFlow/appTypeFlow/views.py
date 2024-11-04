from django.shortcuts import render, redirect 
from .forms import QuizForm
from .models import Question, MBTIResult

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
    questions_per_page = 12 if page < 4 else 14
    start_index = (page - 1) * questions_per_page
    end_index = start_index + questions_per_page

    questions = Question.objects.all()[start_index:end_index]
    total_questions = Question.objects.count()  # Número total de perguntas

    all_labels = [
        ("Mais Falante", "Mais Ouvinte"),
        ("Mais Aberto", "Mais Reservado"),
        ("Mais Impulsivo", "Mais Retraído"),
        ("Mais Social", "Mais Individual"),
        ("Age antes de pensar", "Pensa antes de agir"),
        ("Mais Entusiasmado", "Mais Quieto"),
        ("Prefere Barulho", "Prefere Silêncio"),
        ("Mais Expressivo", "Mais Contido"),
        ("Mais Força", "Mais Delicadeza"),
        ("Mais Agitado", "Mais Calmo"),
        ("Mais Expansivo", "Mais Introspectivo"),
        ("Fala mais do que ouve", "Ouve mais do que fala"),
        ("Pés no chão", "Cheio de ideias"),
        ("Experiência", "Instinto"),
        ("Visão focada em detalhes", "Visão Global"),
        ("Praticidade", "Imaginação"),
        ("Específico e literal", "Metáfora e Analogia"),
        ("Realidade", "Intuição"),
        ("Segurança", "Liberdade"),
        ("Presente", "Futuro"),
        ("Fatos", "Possibilidades"),
        ("Faz", "Cria"),
        ("Concreto", "Abstrato"),
        ("passo a passo", "saltos e de forma indireta"),
        ("Analisador", "Simpatizador"),
        ("Objetivo", "Emocional"),
        ("Razão", "Emoção"),
        ("Crítico", "Aceitável"),
        ("Observador", "Participante"),
        ("Baseado em princípios", "Baseado em valores"),
        ("Pensamento", "Sentimento"),
        ("Convincente", "Comovente"),
        ("Frio", "Caloroso"),
        ("Justiça", "Harmonia"),
        ("Motivado pela realização", "Motivado por ser apreciado"),
        ("Firme", "Gentil"),
        ("Decide rápido", "Dificuldade decidir"),
        ("Pensa estruturado", "Pensa globalmente"),
        ("Organizado", "Deixa acontecer"),
        ("Planejado", "Flexível"),
        ("Decidido", "Impulsivo"),
        ("Controlado", "Espontâneo"),
        ("Limita informação", "Ouve todos os lados"),
        ("Determinado", "Dedicado"),
        ("Valoriza ordem", "Valoriza liberdade"),
        ("Prefere o conhecido", "Prefere o novo"),
        ("Sistemático", "Improvisado"),
        ("Disciplinado", "Sem regras"),
        ("Segue rotina", "Aberto a mudanças"),
        ("Focado em objetivos", "Vê oportunidades")
    ]
    
    labels = all_labels[start_index:end_index]
    question_label_pairs = zip(questions, labels)

    form = QuizForm(request.POST or None, questions=questions)

    if request.method == 'POST':
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
                MBTIResult.objects.create(user=None, mbti_type=mbti_type)
                return redirect('result_view')

    return render(request, f'testes/teste{page}_mbti.html', {
        'form': form,
        'total_questions': total_questions,
        'question_label_pairs': question_label_pairs,
        'page': page,
    })

def result_view(request):
    mbti_type = request.session.get('mbti_type')
    try:
        result = MBTIResult.objects.latest('date_taken')
    except MBTIResult.DoesNotExist:
        result = None

    # Limpa o progresso ao finalizar o teste
    if 'quizProgress' in request.session:
        del request.session['quizProgress']

    return render(request, 'testes/result.html', {'mbti_type': mbti_type, 'result': result})

# Outras views
def home_aluno(request):
    return render(request, 'aluno/home_aluno.html')

def teste1_mbti(request):
    return redirect('quiz_view', page=1)

def teste2_mbti(request):
    return redirect('quiz_view', page=2)

def teste3_mbti(request):
    return redirect('quiz_view', page=3)

def teste4_mbti(request):
    return redirect('quiz_view', page=4)
