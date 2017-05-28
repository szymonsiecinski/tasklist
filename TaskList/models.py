from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from TaskList import polish_timedelta


class Task(models.Model):
    """
    Klasa opisująca zadania do wykonania wraz z opisem
    """
    user = models.ForeignKey(User)
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=4000)
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=timezone.now)
    done = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task', kwargs={'pk': self.pk})

    def clean(self):
        '''
        metoda wykonująca walidację modelu
        :return: 
        '''
        if self.start > self.end:
            # tłumaczenie na angielski: Start date is later than end date.
            raise ValidationError(_("Data zakończenia jest wcześniej niż data rozpoczęcia."))
    
    def finish(self):
        self.done = True
        self.end = timezone.now()

    def calculate_task_time(self):
        return self.end - self.start

    def calculate_real_task_time(self):
        real_task_time = timezone.now() - self.start

        if not self.done:
            return real_task_time

        return self.calculate_task_time()

    def get_localized_task_time(self):
        return polish_timedelta.localize(self.calculate_task_time())

    def get_localized_real_task_time(self):
        return polish_timedelta.localize(self.calculate_real_task_time())