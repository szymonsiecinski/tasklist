from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from TaskList.forms import RegisterUserForm


class LoginView(View):
    """
    odpowiada za obsługę widoku logowania użytkownika
    """

    template_name = "TaskList/login.html"

    def get(self, request):
        context = {
            'user': None,
            'active': 'home'
        }
        return render(request, self.template_name, context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/tasks')
            else:
                return render(request, self.template_name)
        else:
            context = {
                'user': None,
                'response': 'Sprawdź nazwę użytkownika i hasło.'
            }
            return render(request, self.template_name, context)


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
