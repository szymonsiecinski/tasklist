'''
Created on 13 kwi 2016

@author: uzytkownik
'''
from django.contrib.auth import get_user, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import NON_FIELD_ERRORS
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import FormView

from TaskList.models import Task
from forms import ChangePasswordForm


class About(View):
    '''
    Wyświetla stronę z informacjami o projekcie
    '''

    def get(self, request):
        user = get_user(request)
        context = {
            'user': user,
            'active': 'about'
        }
        return render(request, "TaskList/about.html", context=context)


@method_decorator(login_required, 'dispatch')
class UserPage(View):
    def get(self, request):
        user = get_user(request)

        context = {
            'user': user,
            'active': 'user',
            'tasks': Task.objects.filter(user=user.pk).count(),
            'tasks_done': Task.objects.filter(user=user.pk, done=True).count(),
            'tasks_todo': Task.objects.filter(user=user.pk, done=False).count()
        }
        return render(request, "TaskList/user_page.html", context=context)


@method_decorator(login_required, 'dispatch')
class ChangePasswordView(FormView):

    template_name = "TaskList/change_password.html"
    form_class = ChangePasswordForm
    success_url = reverse_lazy('user_page')

    def form_valid(self, form):
        user_name = self.request.user
        user = User.objects.get(username__exact=user_name)

        cleaned_data = form.clean()
        new_password = cleaned_data['password']

        # sprawdzanie, czy podano obecne hasło jako nowe
        if user.check_password(new_password):
            # dostęp do chronionego pola z błędami w formularzu
            # rozwiązanie z https://gist.github.com/vero4karu/3b62a13bdce7fe4178ac
            form._errors[NON_FIELD_ERRORS] = ErrorList([
                'Podano obecne hasło'
            ])
            return self.form_invalid(form)

        user.set_password(new_password)
        user.save()

        # ponowny login po zmianie hasła
        login(self.request, user)

        return super(ChangePasswordView, self).form_valid(form)

    # def post(self, request):
    #     user_name = get_user(request)
    #     user = User.objects.get(username__exact=user_name)
    #
    #     password = request.POST['password']
    #     conf_password = request.POST['conf_password']
    #
    #     context = {
    #         'user': user
    #     }
    #
    #     new_password_is_valid = password == conf_password and not user.check_password(password)
    #     if new_password_is_valid:
    #         user.set_password(password)
    #         user.save()
    #
    #         # ponowny login po zmianie hasła
    #         login(request, user)
    #
    #     # sprawdzanie, czy nowe hasło jest takie, jak obecne
    #     elif user.check_password(password):
    #         context['response']= 'Podano obecne hasło.'
    #         return render(request, self.TEMPLATE_NAME, context)
    #     else:
    #         context['response']= 'Podane hasła się nie zgadzają.'
    #         return render(request, self.TEMPLATE_NAME, context)
    #
    #     return redirect("user_page")
