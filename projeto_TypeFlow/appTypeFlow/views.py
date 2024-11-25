from django.shortcuts import render, redirect
from .forms import QuizForm, CadastroForm
from .models import Pergunta, resultadoMBTI
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect ('/professor/') # Redireciona professores para a página deles
        return redirect('/home_aluno')  # Redireciona alunos para a página deles
    else:
        messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login/cadastro/login.html')

from django.shortcuts import render

def cadastro(request):
    if request.method == "POST":
        # Inicializa o formulário com os dados enviados
        form = CadastroForm(request.POST)
        if form.is_valid():
            # Se os dados forem válidos, cria o usuário
            nome = form.cleaned_data["nome"]
            email = form.cleaned_data["email"]
            senha = form.cleaned_data["senha"]

            try:
                # Criar o usuário no banco de dados
                user = User.objects.create_user(username=email, email=email, password=senha)
                user.first_name = nome
                user.save()

                messages.success(request, "Cadastro realizado com sucesso! Faça login para continuar.")
                return redirect("login_usuario")  # Substitua pelo nome da rota de login
            except Exception as e:
                messages.error(request, f"Erro ao criar conta: {str(e)}")
        else:
            # Se o formulário não for válido, exibe os erros
            messages.error(request, "Por favor, corrija os erros no formulário.")
    else:
        # Para requisições GET, inicializa um formulário vazio
        form = CadastroForm()

    # Renderiza o template com o formulário
    return render(request, 'login/cadastro/cadastro.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/')
    

# Função para calcular o tipo MBTI com base nas respostas
def calculate_mbti(answers):
    # Dicionário para armazenar as pontuações para cada dimensão MBTI
    scores = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}

    # Loop para somar pontuações com base nas respostas dadas
    for question_id, choice in answers.items():
        # Obter a pergunta correspondente a partir do ID
        question = Pergunta.objects.get(id=question_id.split('_')[-1])

        # Incrementar a pontuação dependendo da dimensão da pergunta
        if question.dimension == 'EI':
            scores[choice] += 1

    # Construir o tipo MBTI com base nas pontuações acumuladas
    mbti_type = (
        ('E' if scores['E'] > scores['I'] else 'I') +
        ('S' if scores['S'] > scores['N'] else 'N') +
        ('T' if scores['T'] > scores['F'] else 'F') +
        ('J' if scores['J'] > scores['P'] else 'P')
    )

    return mbti_type

# View principal para o teste de MBTI
def quiz_view(request, page=1):
    # Definir o número de perguntas por página (última página tem mais perguntas)
    questions_per_page = 12 if page < 4 else 14

    # Calcular o índice inicial e final das perguntas para a página atual
    start_index = (page - 1) * questions_per_page
    end_index = start_index + questions_per_page

    # Obter as perguntas do banco de dados para a página atual
    questions = Pergunta.objects.all()[start_index:end_index]
    total_questions = Pergunta.objects.count()  # Número total de perguntas no teste

    # Lista de rótulos para as opções das perguntas
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

    # Emparelhar perguntas com rótulos
    labels = all_labels[start_index:end_index]
    question_label_pairs = zip(questions, labels)

    # Inicializar o formulário com as perguntas da página atual
    form = QuizForm(request.POST or None, questions=questions)

    # Processar o envio do formulário (método POST)
    if request.method == 'POST':
        if form.is_valid():
            # Armazenar as respostas no dicionário da sessão
            answers = request.session.get('quiz_answers', {})
            for key, value in form.cleaned_data.items():
                answers[key] = value
            request.session['quiz_answers'] = answers

            # Redirecionar para a próxima página se houver mais páginas
            if page < 4:
                return redirect('quiz_view', page=page + 1)
            else:
                # Calcular o tipo MBTI após a última página
                mbti_type = calculate_mbti(answers)
                request.session['mbti_type'] = mbti_type

                # Salvar o resultado no banco de dados
                resultadoMBTI.objects.create(user=None, mbti_type=mbti_type)

                # Redirecionar para a página de resultados
                return redirect('result_view')

    # Renderizar a página com o formulário e perguntas
    return render(request, f'testes/teste{page}_mbti.html', {
        'form': form,
        'total_questions': total_questions,
        'question_label_pairs': question_label_pairs,
        'page': page,
    })

# View para exibir o resultado após a conclusão do teste
def result_view(request):
    # Recuperar o tipo MBTI da sessão
    mbti_type = request.session.get('mbti_type')

    # Tentar obter o último resultado salvo no banco de dados
    try:
        result = resultadoMBTI.objects.latest('date_taken')
    except resultadoMBTI.DoesNotExist:
        result = None

    # Limpar o progresso da sessão ao finalizar o teste
    if 'quizProgress' in request.session:
        del request.session['quizProgress']

    return render(request, 'testes/result.html', {'mbti_type': mbti_type, 'result': result})

# Outras views para redirecionar para a página inicial do teste
def home_aluno(request):
    return render(request, 'aluno/home_aluno.html')

# Redirecionar para a página 1 do teste
def teste1_mbti(request):
    return redirect('quiz_view', page=1)

# Redirecionar para a página 2 do teste
def teste2_mbti(request):
    return redirect('quiz_view', page=2)

# Redirecionar para a página 3 do teste
def teste3_mbti(request):
    return redirect('quiz_view', page=3)

# Redirecionar para a página 4 do teste
def teste4_mbti(request):
    return redirect('quiz_view', page=4)
