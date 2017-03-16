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


@method_decorator(login_required, name='dispatch')
class TaskList(ListView):
    '''
    Lista zadań
    '''
    model = Task
    allow_empty = True
    context = {
        'user': None
    }


@method_decorator(login_required, name='dispatch')
class TaskCreate(CreateView):
    '''
    Tworzenie nowego zadania
    '''
    model = Task
    success_url = reverse_lazy('task_list')
    fields = ['name', 'description', 'start', 'end', 'done']


@method_decorator(login_required, name='dispatch')
class TaskUpdate(UpdateView):
    '''zmiana zadania'''
    model = Task
    success_url = reverse_lazy('task_list')
    fields = ['name', 'description', 'start', 'end', 'done']


@method_decorator(login_required, name='dispatch')
class TaskDelete(DeleteView):
    '''usuwanie zadania'''
    model = Task
    login_required = True
    success_url= reverse_lazy('task_list')


@method_decorator(login_required, name='dispatch')
class TaskListDone(ListView):
    '''pokazuje wykonane zadania'''
    done = True
    allow_empty = True
    queryset = Task.objects.filter(done=done)


@method_decorator(login_required, name='dispatch')
class TaskListToDo(ListView):
    '''pokazuje zadania do wykonania'''
    done = False
    allow_empty = True
    queryset = Task.objects.filter(done=done)


class About(View):
    def get(self, request):
        user = get_user(request)
        context = {
            'user': user
        }
        return render(request, "TaskList/about.html", context=context)