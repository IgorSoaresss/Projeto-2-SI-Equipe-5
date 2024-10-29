from django import forms
from .models import Question

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        questions = Question.objects.all()
        for question in questions:
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.text,
                choices=[('E', 'Extroversão'), ('I', 'Introversão')] if question.dimension == 'EI' else
                        [('S', 'Sensação'), ('N', 'Intuição')] if question.dimension == 'SN' else
                        [('T', 'Pensamento'), ('F', 'Sentimento')] if question.dimension == 'TF' else
                        [('J', 'Julgamento'), ('P', 'Percepção')]
            )
