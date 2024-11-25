from django import forms
from .models import Question

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
from django import forms

class CadastroForm(forms.Form):
    nome = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome'}),
        label="Nome"
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Digite seu email'}),
        label="Email"
    )
    senha = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}),
        label="Senha"
    )
    confirmar_senha = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'}),
        label="Confirmar Senha"
    )

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if senha != confirmar_senha:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data
