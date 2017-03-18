from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from models import Task


@method_decorator(login_required, name='dispatch')
class TaskList(ListView):
    '''
    Lista zadań
    '''
    allow_empty = True

    def get_queryset(self):
        '''
        zwraca listę zadań dla użytkownika
        :return: lista zadań dla bieżącego użytkownika
        '''
        return Task.objects.filter(user=self.request.user.pk)

    def get_context_data(self, **kwargs):
        '''
        zwraca kontekst danych widoku
        :param kwargs: zmienne kontekstu
        :return: kontekst widuoku
        '''
        context = super(TaskList, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator(login_required, name='dispatch')
class TaskListDone(ListView):
    '''pokazuje wykonane zadania'''
    done = True
    allow_empty = True
    queryset = Task.objects.filter(done=done)

    def get_context_data(self, **kwargs):
        '''
        zwraca kontekst danych widoku
        :param kwargs: zmienne kontekstu
        :return: kontekst widuoku
        '''
        context = super(TaskListDone, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator(login_required, name='dispatch')
class TaskListToDo(ListView):
    '''pokazuje zadania do wykonania'''
    done = False
    allow_empty = True
    queryset = Task.objects.filter(done=done)

    def get_context_data(self, **kwargs):
        '''
        zwraca kontekst danych widoku
        :param kwargs: zmienne kontekstu
        :return: kontekst widuoku
        '''
        context = super(TaskListToDo, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context