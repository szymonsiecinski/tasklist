from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from datetimewidget.widgets import DateTimeWidget

from TaskList.models import Task


class RegisterUserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(), label='Hasło')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Powtórz hasło')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get("password")
        conf_password = self.cleaned_data.get("confirm_password")

        return self.cleaned_data


class ChangePasswordForm(forms.Form):

    password = forms.CharField(widget=forms.PasswordInput(), label='Hasło')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Powtórz hasło')

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean(self):
        password = self.cleaned_data.get("password")
        conf_password = self.cleaned_data.get("confirm_password")

        if password != conf_password:
            raise forms.ValidationError(_("Podane hasła się nie zgadzają."))

        return self.cleaned_data


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
