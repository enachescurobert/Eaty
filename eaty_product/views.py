from eaty_product.serializers import ProductSerializer, ProductTypeSerializer
from eaty_product.models import ProductType, Product
from rest_framework import generics
from eaty_product.forms import ProductTypeForm
from .models import ProductType
from django.shortcuts import render, redirect


class ProductTypeList(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

def list_products(request):
    products = ProductType.objects.all()
    return render(request,"app/components/product-type/product-type.template.html", {'products':products})

def create_product(request):
    form = ProductTypeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request,'app/components/product-type/products-form.template.html', {'form':form})

def update_product(request, id):
    product = ProductType.objects.get(id=id)
    form = ProductTypeForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'app/components/product-type/products-form.template.html', {'form':form, 'product':product})

def delete_product(request, id):
    product = ProductType.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('list_products')

    return render(request, 'app/components/product-type/prod-delete-confirm.template.html')
