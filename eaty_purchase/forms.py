from django import forms
from django.contrib.auth.models import User, Group
from .models import Session

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('user','coffe','cake')