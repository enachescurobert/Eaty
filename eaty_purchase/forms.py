from django import forms
from django.contrib.auth.models import User, Group
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'