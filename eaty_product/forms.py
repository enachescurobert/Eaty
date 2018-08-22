from django import forms
from .models import ProductType, Product

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
