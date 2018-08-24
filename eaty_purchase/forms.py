from django import forms
from django.contrib.auth.models import User, Group
from .models import Purchase

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'