"""TaskList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from TaskList.views import *
from TaskList.auth_views import *
from TaskList.list_views import *
from TaskList.manipulation_views import *

urlpatterns = [
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^register$', RegisterView.as_view(), name='register'),
    url(r'^logout$', Logout.as_view(), name='logout'),
    url(r'^accounts/login/$', LoginView.as_view()),
    url(r'^about$', AboutView.as_view(), name='about'),
    url(r'^user', UserPageView.as_view(), name='user_page'),
    url(r'^changepass', ChangePasswordView.as_view(), name='change_password'),
    url(r'^tasks$', TaskList.as_view(), name='task_list'),
    url(r'^task/details/(?P<pk>\d+)$', TaskDetailsView.as_view(), name='task_details'),
    url(r'^task/new/$', TaskCreate.as_view(), name='task_new'),
    url(r'^task/edit/(?P<pk>\d+)$', TaskUpdate.as_view(), name='task_edit'),
    url(r'^task/delete/(?P<pk>\d+)$', TaskDelete.as_view(), name='task_delete'),
    url(r'^task/finish/(?P<pk>\d+)$', TaskFinish.as_view(), name='task_finish'),
    url(r'^tasks/done/$', TaskListFilteredByFlagDone.as_view(done=True), name='task_list_done'),
    url(r'^tasks/todo/$', TaskListFilteredByFlagDone.as_view(done=False), name='task_list_todo'),
]
