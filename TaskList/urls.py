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

from TaskList import views, auth_views, list_views, manipulation_views

urlpatterns = [
    url(r'^$', auth_views.LoginView.as_view(), name='login'),
    url(r'^register$', auth_views.RegisterView.as_view(), name='register'),
    url(r'^logout$', auth_views.Logout.as_view(), name='logout'),
    url(r'^about$', views.About.as_view(), name='about'),
    url(r'^tasks$', list_views.TaskList.as_view(), name='task_list'),
    url(r'^task/new/$', manipulation_views.TaskCreate.as_view(), name='task_new'),
    url(r'^task/edit/(?P<pk>\d+)$',
        manipulation_views.TaskUpdate.as_view(), name='task_edit'),
    url(r'^task/delete/(?P<pk>\d+)$',
        manipulation_views.TaskDelete.as_view(template_name="TaskList/task_delete.html"),
        name='task_delete'),
    url(r'^tasks/done/$',
        list_views.TaskListFilteredByFlagDone.as_view(done=True, template_name = "TaskList/task_list_filt.html"),
        name='task_list_done'),
    url(r'^tasks/todo/$',
        list_views.TaskListFilteredByFlagDone.as_view(done=False, template_name = "TaskList/task_list_filt.html"),
        name='task_list_todo'),
    url(r'^accounts/login/$', auth_views.LoginView.as_view()),
]
