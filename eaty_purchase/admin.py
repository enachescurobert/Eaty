from django.contrib import admin
from .models import Session, Purchase, Profile

# Register your models here.
admin.site.register(Session)
admin.site.register(Purchase)
admin.site.register(Profile)