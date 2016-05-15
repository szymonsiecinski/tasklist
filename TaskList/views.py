'''
Created on 13 kwi 2016

@author: uzytkownik
'''

from django.views.generic import TemplateView, ListView
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
    model = Task
    success_url = reverse_lazy('task_list')
    fields = ['name', 'description', 'start', 'end', 'done']
    
class TaskDelete(DeleteView):
    model = Task
    url= reverse_lazy('task_list')

class TaskListDone(ListView):
    done = True
    queryset = Task.objects.filter(done=done)
    
class TaskListToDo(ListView):
    done = False
    queryset = Task.objects.filter(done=done)