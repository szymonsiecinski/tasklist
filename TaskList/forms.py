from django import forms
from django.utils.translation import ugettext_lazy as _

from TaskList.models import Task


class TaskEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TaskEditForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Task
        fields = ['name', 'description', 'start', 'end', 'done']
        labels = {
            'name': _('Nazwa'),
            'description': _('Opis'),
            'start': _('Początek'),
            'end': _('Koniec'),
            'done': _('Wykonane')
        }
        help_texts = {
            'name': _('Nazwa zadania'),
            'description': _('Opis zadania (do 4000 znaków)'),
            'start': _('Data i godzina rozpoczęcia zadania'),
            'end': _('Data i godzina zakończenia zadania'),
            'done': _('Zaznacz, jeżeli zadanie zostało wykonane')
        }
        error_messages = {
            'name': {
                'max_length': _("Nazwa jest za długa."),
            },
        }
        # widgets = {
        #     'content': forms.Textarea(attrs={'cols': 80, 'rows': 20})
        # }
