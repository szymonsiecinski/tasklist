from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView

from TaskList.auth_forms import RegisterUserForm, LoginForm


class LoginView(FormView):
    """
    odpowiada za obsługę widoku logowania użytkownika
    """
    template_name = "TaskList/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("task_list")

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['user'] = None
        context['active'] = "home"
        return context

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(self.request, user)
                return super(LoginView, self).form_valid(form)
        else:
            form.add_error(None, _("Podano niepoprawną nazwę użytkownika lub hasło."))
            return self.form_invalid(form)


class RegisterView(CreateView):
    template_name = "TaskList/register.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context_data = super(RegisterView, self).get_context_data(**kwargs)
        context_data['user'] = None
        return context_data
    
    def form_valid(self, form):
        form_data = form.clean()
        
        try:
            User.objects.get(username__exact=form_data['username'])
            form.add_error('username', _('Użytkownik o tej nazwie już istnieje.'))
            return super(RegisterView, self).form_invalid(form)

        except ObjectDoesNotExist:
            # Wykonuj, jeżeli nie ma takiego użytkownika (happy path)
            user = User(username=form_data['username'])
            user.set_password(form_data['password'])
            user.save()
            return super(RegisterView, self).form_valid(form)


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
