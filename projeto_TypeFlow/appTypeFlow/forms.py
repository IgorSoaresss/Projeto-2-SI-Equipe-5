from django import forms
from .models import Pergunta

class QuizForm(forms.Form):
    def __init__(self, *args, questions=None, **kwargs):
        super().__init__(*args, **kwargs)
        if questions:
            for question in questions:
                self.fields[f'question_{question.id}'] = forms.ChoiceField(
                    label=question.text,
                    choices=[('A', 'Opção A'), ('B', 'Opção B')],  # Adicione opções conforme necessário
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
