'''
Created on 13 kwi 2016

@author: uzytkownik
'''

from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime

class Task(models.Model):
    '''
    Klasa opisująca zadania do wykonania wraz z opisem
    '''
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=4000)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task', kwargs={'id': self.id})
    
    def finish(self):
        self.done = True
        self.end = datetime()