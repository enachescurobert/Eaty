from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum, F, Value

class Session(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='sessions')
    coffe = models.FloatField(default=0)
    cake = models.FloatField(default=0)

    coffetotal = models.FloatField(null=True, blank=True)
    caketotal = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)

    start_date = models.DateTimeField('date published',null=True, blank=True)
    end_date = models.DateTimeField('date finished', null=True, blank=True)

    def coffe_total(self):
        return self.coffe * 0.1

    def cake_total(self):
        return self.cake * 0.5
    
    def value_total(self):
        return self.coffetotal * self.caketotal

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')   
    
    value = models.FloatField(null=True, blank=True)



    def __str__(self):
        return 'The debt of {} is {} '.format(self.user, self.value)






