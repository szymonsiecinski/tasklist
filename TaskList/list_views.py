from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from TaskList.models import Task


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


@method_decorator(login_required, 'dispatch')
class TaskListFilteredByFlagDone(ListView):
    '''pokazuje wykonane zadania'''
    done = True
    allow_empty = True
    template_name = "TaskList/task_list_filt.html"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user.pk, done=self.done)

    def get_context_data(self, **kwargs):
        '''
        zwraca kontekst danych widoku
        :param kwargs: zmienne kontekstu
        :return: kontekst widuoku
        '''
        context = super(TaskListFilteredByFlagDone, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context