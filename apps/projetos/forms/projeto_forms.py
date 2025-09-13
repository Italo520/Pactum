# apps/projetos/forms/projeto_forms.py
from django import forms
from ..models.projeto import Projeto

from django import forms
from apps.projetos.models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = [
            'cod_projeto',
            'nome',
            'data_inicio',
            'data_encerramento',
            'valor',
            'situacao',
        ]
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_encerramento': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'data_inicio': 'Data de Início',
            'data_encerramento': 'Data de Encerramento',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona classes do Bootstrap aos campos
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, (forms.CheckboxInput, forms.Select)):
                field.widget.attrs.update({'class': 'form-control'})