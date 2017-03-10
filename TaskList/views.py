'''
Created on 13 kwi 2016

@author: uzytkownik
'''

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from TaskList.models import Task

class TaskList(ListView):
    '''
    Lista zadań
    '''
    model = Task


class TaskCreate(CreateView):
    '''
    Tworzenie nowego zadania
    '''
    model = Task
    success_url = reverse_lazy('task_list')
    fields = ['name', 'description', 'start', 'end', 'done']


class TaskUpdate(UpdateView):
    '''zmiana zadania'''
    model = Task
    success_url = reverse_lazy('task_list')
    fields = ['name', 'description', 'start', 'end', 'done']


class TaskDelete(DeleteView):
    '''usuwanie zadania'''
    model = Task
    success_url= reverse_lazy('task_list')


class TaskListDone(ListView):
    '''pokazuje wykonane zadania'''
    done = True
    queryset = Task.objects.filter(done=done)


class TaskListToDo(ListView):
    '''pokazuje zadania do wykonania'''
    done = False
    queryset = Task.objects.filter(done=done)
