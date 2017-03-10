'''
Created on 13 kwi 2016

@author: uzytkownik
'''
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime


class Task(models.Model):
    '''
    Klasa opisująca zadania do wykonania wraz z opisem
    '''
    user = models.ForeignKey(User)
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=4000)
    start = models.DateTimeField(default=datetime.now)
    end = models.DateTimeField(default=datetime.now)
    done = models.BooleanField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task', kwargs={'pk': self.pk})
    
    def finish(self):
        self.done = True
        self.end = datetime()