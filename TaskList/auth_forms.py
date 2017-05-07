from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
        help_texts = {
            'username': ""
        }

    def clean(self):
        return self.cleaned_data


class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Hasło')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Powtórz hasło')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password']

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get("password")
        conf_password = self.cleaned_data.get("confirm_password")

        if password != conf_password:
            raise forms.ValidationError(_("Podane hasła się nie zgadzają."))

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
