from pyexpat import model
from django import forms
from .models import Tarefas

class tarefasForm(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = [
            'nome',
            'prioridade',
            'descriçao',
        ]