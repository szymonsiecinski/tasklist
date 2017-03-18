from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, UpdateView

from TaskList.models import Task


@method_decorator(login_required, name='dispatch')
class TaskCreate(CreateView):
    '''
    Tworzenie nowego zadania
    '''
    model = Task
    success_url = reverse_lazy('task_list')
    fields = ['name', 'description', 'start', 'end', 'done']

    def get_context_data(self, **kwargs):
        '''
        zwraca kontekst danych widoku
        :param kwargs: zmienne kontekstu
        :return: kontekst widuoku
        '''
        context = super(TaskCreate, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class TaskUpdate(UpdateView):
    '''zmiana zadania'''
    model = Task
    success_url = reverse_lazy('task_list')
    fields = ['name', 'description', 'start', 'end', 'done']

    def get_context_data(self, **kwargs):
        '''
        zwraca kontekst danych widoku
        :param kwargs: zmienne kontekstu
        :return: kontekst widuoku
        '''
        context = super(TaskUpdate, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskUpdate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class TaskDelete(DeleteView):
    '''usuwanie zadania'''
    model = Task
    login_required = True
    success_url= reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        '''
        zwraca kontekst danych widoku
        :param kwargs: zmienne kontekstu
        :return: kontekst widuoku
        '''
        context = super(TaskDelete, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context