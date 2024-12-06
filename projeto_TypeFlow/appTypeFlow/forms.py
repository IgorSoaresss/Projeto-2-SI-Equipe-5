from django import forms
from .models import Question, Turmas, CustomUser

class QuizForm(forms.Form):
    def __init__(self, *args, questions=None, **kwargs):
        super().__init__(*args, **kwargs)
        if questions:
            for question in questions:
                # Identificar a dimensão da pergunta (EI, SN, TF, JP)
                if question.dimension == 'EI':
                    choices = [('E', 'Extrovertido'), ('I', 'Introvertido')]
                elif question.dimension == 'SN':
                    choices = [('S', 'Sensing'), ('N', 'Intuition')]
                elif question.dimension == 'TF':
                    choices = [('T', 'Thinking'), ('F', 'Feeling')]
                elif question.dimension == 'JP':
                    choices = [('J', 'Judging'), ('P', 'Perceiving')]
                else:
                    continue  # Caso uma dimensão não seja reconhecida, pula a pergunta

                # Criar o campo ChoiceField para cada pergunta com base na dimensão
                self.fields[f'question_{question.id}'] = forms.ChoiceField(
                    label=question.text,
                    choices=choices,
                    widget=forms.RadioSelect
                )

class CadastroForm(forms.ModelForm):
    confirmar_senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'}),
        label="Confirmar Senha"
    )

    class Meta:
        model = CustomUser
        fields = ['nome', 'email', 'senha', 'turma', 'periodo']
        widgets = {
            'turma': forms.Select(choices=[('SI', 'Sistemas de Informação'), ...]),
            'periodo': forms.NumberInput(attrs={'min': 1, 'max': 10}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@cesar.school'):
            raise forms.ValidationError("O e-mail deve ser do domínio '@cesar.school'.")
        return email

class TurmaForm(forms.ModelForm):

    class Meta:
        model = Turmas
        fields = ['curso', 'periodo', 'turma']
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-select'}),  # Dropdown para cursos
            'periodo': forms.Select(attrs={'class': 'form-select'}),  # Dropdown para períodos
            'turma': forms.Select(attrs={'class': 'form-select'}),  # Dropdown para turmas
        }