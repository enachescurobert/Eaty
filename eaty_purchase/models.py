from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Session(models.Model):
    start_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('date finished')
    def __str__(self):
        return self.start_date

class Purchase(models.Model):
    value = models.FloatField()
    user = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE, related_name='purchases')

    def __str__(self):
        return 'The debt of %s is %s $' % (self.user, self.value)