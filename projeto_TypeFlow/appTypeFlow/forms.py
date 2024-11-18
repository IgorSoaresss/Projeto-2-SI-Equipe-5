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
