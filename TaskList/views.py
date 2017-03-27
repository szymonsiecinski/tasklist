'''
Created on 13 kwi 2016

@author: uzytkownik
'''
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
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
            'user': user
        }
        return render(request, "TaskList/about.html", context=context)


@method_decorator(login_required, 'dispatch')
class UserPage(View):
    def get(self, request):

        user = get_user(request)
        context = {
            'user': user,
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

        if password == conf_password and not user.check_password(password):
            user.set_password(password)
            user.save()
        elif user.check_password(password):
            context = {
                'user': user_name,
                'response': 'Podano obecne hasło.'
            }
            return render(request, self.TEMPLATE_NAME, context)
        else:
            context = {
                'user': user_name,
                'response': 'Podane hasła się nie zgadzają.'
            }
            return render(request, self.TEMPLATE_NAME, context)

        return HttpResponseRedirect("/")
