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
from TaskList import views

urlpatterns = [
    url(r'^$', views.TaskList.as_view(), name='task_list'),
    url(r'^new/$', views.TaskCreate.as_view(), name='task_new'),
    url(r'^edit/(?P<pk>\d+)$', views.TaskUpdate.as_view(), name='task_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.TaskDelete.as_view(template_name="TaskList/task_delete.html"), name='task_delete'),
    url(r'^done/$', views.TaskListDone.as_view(template_name = "TaskList/task_list_filt.html"), name='task_list_done'),
    url(r'^todo/$', views.TaskListToDo.as_view(template_name = "TaskList/task_list_filt.html"), name='task_list_todo')
]
