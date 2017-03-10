from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class LoginView(View):
    '''
    odpowiada za obsługę widoku logowania użytkownika
    '''

    TEMPLATE_NAME = "TaskList/login.html"

    def get(self, request):
        context = {
            'user': None
        }
        return render(request, self.TEMPLATE_NAME, context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/tasks')
            else:
                return render(request, self.TEMPLATE_NAME)
        else:
            context = {
                'user': None,
                'response': 'Sprawdź nazwę użytkownika i hasło.'
            }
            return render(request, self.TEMPLATE_NAME, context)


class RegisterView(View):
    TEMPLATE_NAME = "TaskList/register.html"

    def get(self, request):
        context = {
            'user': None
        }
        return render(request, self.TEMPLATE_NAME, context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        conf_password = request.POST['conf_password']

        if password == conf_password:
            user = User(username=username)
            user.set_password(password)
            user.save()
        else:
            context = {
                'user': None,
                'response': 'Podane hasła się nie zgadzają.'
            }
            return render(request, self.TEMPLATE_NAME, context)

        return HttpResponseRedirect("/")


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')