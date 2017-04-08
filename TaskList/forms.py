from django import forms
from django.utils.translation import ugettext_lazy as _
from datetimewidget.widgets import DateTimeWidget

from TaskList.models import Task


class TaskEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TaskEditForm, self).__init__(*args, **kwargs)

    class Meta:
        DateTimeOptions = {
            'language': 'pl',
            'showMeridian': 'true'
        }

        model = Task
        fields = ['name', 'description', 'start', 'end']
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
            'description': {
                'max_length': _("Opis jest za długi."),
            },
        }
        widgets = {
            'start': DateTimeWidget(options=DateTimeOptions, usel10n=True, bootstrap_version=3),
            'end': DateTimeWidget(options=DateTimeOptions, usel10n=True, bootstrap_version=3)
        }
