from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum, F, Value

class Session(models.Model):
    start_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('date finished')
    def __str__(self):
        return self.start_date

class Purchase(models.Model):
    value = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')

    def __str__(self):
        return 'The debt of {} is {} '.format(self.user, self.value)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    coffe = models.FloatField(null=True)
    cake = models.FloatField(null=True)

    coffetotal = models.FloatField(null=True)
    caketotal = models.FloatField(null=True)
    
    total = models.FloatField(null=True)