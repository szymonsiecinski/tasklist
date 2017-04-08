from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

import forms
from TaskList.models import Task


@method_decorator(login_required, name='dispatch')
class TaskCreate(CreateView):
    '''
    Tworzenie nowego zadania
    '''
    model = Task
    success_url = reverse_lazy('task_list')
    form_class = forms.TaskEditForm

    def get_context_data(self, **kwargs):
        '''
        zwraca kontekst danych widoku
        :param kwargs: zmienne kontekstu
        :return: kontekst widuoku
        '''
        context = super(TaskCreate, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['edit'] = True
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class TaskUpdate(UpdateView):
    '''zmiana zadania'''
    model = Task
    success_url = reverse_lazy('task_list')
    form_class = forms.TaskEditForm

    def get_context_data(self, **kwargs):
        '''
        zwraca kontekst danych widoku
        :param kwargs: zmienne kontekstu
        :return: kontekst widuoku
        '''
        context = super(TaskUpdate, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['edit'] = False
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskUpdate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class TaskDelete(DeleteView):
    '''usuwanie zadania'''
    model = Task
    login_required = True
    template_name = "TaskList/task_delete.html"
    success_url = reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        '''
        zwraca kontekst danych widoku
        :param kwargs: zmienne kontekstu
        :return: kontekst widoku
        '''
        context = super(TaskDelete, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator(login_required, name='dispatch')
class TaskFinish(View):
    def get(self, request, **kwargs):
        task = Task.objects.get(user=self.request.user.pk, pk=kwargs['pk'])
        task.finish()
        task.save()

        return HttpResponseRedirect(reverse_lazy('task_list'))
