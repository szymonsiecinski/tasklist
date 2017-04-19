'''
Created on 13 kwi 2016

@author: uzytkownik
'''
from django.contrib.auth import get_user, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from TaskList.models import Task


class About(View):
    '''
    Wyświetla stronę z informacjami o projekcie
    '''

    def get(self, request):
        user = get_user(request)
        context = {
            'user': user,
            'active': 'about'
        }
        return render(request, "TaskList/about.html", context=context)


@method_decorator(login_required, 'dispatch')
class UserPage(View):
    def get(self, request):

        user = get_user(request)
        context = {
            'user': user,
            'active': 'user',
            'tasks': Task.objects.filter(user=user.pk).count(),
            'tasks_done': Task.objects.filter(user=user.pk, done=True).count(),
            'tasks_todo': Task.objects.filter(user=user.pk, done=False).count()
        }
        return render(request, "TaskList/user_page.html", context=context)


@method_decorator(login_required, 'dispatch')
class ChangePasswordView(View):
    TEMPLATE_NAME = "TaskList/change_password.html"

    def get(self, request):
        user = get_user(request)
        context = {
            'user': user,
        }
        return render(request, self.TEMPLATE_NAME, context=context)

    def post(self, request):
        user_name = get_user(request)
        user = User.objects.get(username__exact=user_name)

        password = request.POST['password']
        conf_password = request.POST['conf_password']

        context = {
            'user': user
        }

        new_password_is_valid = password == conf_password and not user.check_password(password)
        if new_password_is_valid:
            user.set_password(password)
            user.save()

            # ponowny login po zmianie hasła
            login(request, user)

        # sprawdzanie, czy nowe hasło jest takie, jak obecne
        elif user.check_password(password):
            context['response']= 'Podano obecne hasło.'
            return render(request, self.TEMPLATE_NAME, context)
        else:
            context['response']= 'Podane hasła się nie zgadzają.'
            return render(request, self.TEMPLATE_NAME, context)

        return redirect("user_page")
