from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from TaskList.models import Task


# class DateTimeWidget(forms.Widget):
#     template_name = 'datetime_widget.html'
#
#     def __init__(self, **kwargs):
#         super(DateTimeWidget, self).__init__(**kwargs)
#
#     def render(self, name, value, attrs=None):
#         context={
#             'value': value,
#             'id': name
#         }
#         return mark_safe(render_to_string(self.template_name, context))


class TaskEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TaskEditForm, self).__init__(*args, **kwargs)

    class Meta:
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
        }
        # widgets = {
        #     'start': DateTimeWidget()
        # }
