'''
Created on 13 kwi 2016

@author: uzytkownik
'''

from django.http import HttpResponse
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
    fields = ['name', 'description', 'start', 'end']
    
class TaskUpdate(UpdateView):
    model = Task
    success_url = reverse_lazy('task_list')
    fields = ['name', 'description', 'start', 'end']
    
class TaskDelete(DeleteView):
    model = Task
    success_url= reverse_lazy('task_list')