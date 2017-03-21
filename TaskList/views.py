'''
Created on 13 kwi 2016

@author: uzytkownik
'''
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
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