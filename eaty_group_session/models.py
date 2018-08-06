from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Session(models.Model):
    debut_date = models.DateTimeField('date published')
    finish_date = models.DateTimeField('date finished')
    def __str__(self):
        return self.debut_date

class Purchase(models.Model):
    value_number = models.IntegerField()
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE,)
    
    def __str__(self):
        return 'The debt of %s is %s $' % (self.user, self.value_number)