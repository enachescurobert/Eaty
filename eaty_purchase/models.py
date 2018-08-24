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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')

    coffe = models.FloatField(default=0)
    cake = models.FloatField(default=0)

    coffetotal = models.FloatField(null=True, blank=True)
    caketotal = models.FloatField(null=True, blank=True)
    
    value = models.FloatField(null=True, blank=True)

    def coffe_total(self):
        return self.coffe * 0.1

    def cake_total(self):
        return self.cake * 0.5
    
    def value_total(self):
        return self.coffetotal * self.caketotal

    def __str__(self):
        return 'The debt of {} is {} '.format(self.user, self.value)






