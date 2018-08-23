from eaty_product.serializers import ProductSerializer, ProductTypeSerializer
from eaty_product.models import ProductType, Product
from rest_framework import generics
from eaty_product.forms import ProductTypeForm, ProductForm
from .models import ProductType, Product
from django.shortcuts import render, redirect

# REST API for ProductType
class ProductTypeList(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

# REST API FOR Product
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Product Type API
def list_producttypes(request):
    producttypes = ProductType.objects.all()
    return render(request,"app/pages/Django-ProductType-API/product-type.template.html", {'producttypes':producttypes})

def create_producttype(request):
    form = ProductTypeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_producttypes')

    return render(request,'app/pages/Django-ProductType-API/producttypes-form.template.html', {'form':form})

def update_producttype(request, id):
    producttype = ProductType.objects.get(id=id)
    form = ProductTypeForm(request.POST or None, instance=producttype)

    if form.is_valid():
        form.save()
        return redirect('list_producttypes')

    return render(request, 'app/pages/Django-ProductType-API/producttypes-form.template.html', {'form':form, 'producttype':producttype})

def delete_producttype(request, id):
    producttype = ProductType.objects.get(id=id)

    if request.method == 'POST':
        producttype.delete()
        return redirect('list_producttypes')

    return render(request, 'app/pages/Django-ProductType-API/product-type-delete-confirm.template.html')

#Product API
def list_products(request):
    products = Product.objects.all()
    return render(request,"app/pages/Django-Product-API/product.template.html", {'products':products})

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request,'app/pages/Django-Product-API/products-form.template.html', {'form':form})

def update_product(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'app/pages/Django-Product-API/products-form.template.html', {'form':form, 'product':product})

def delete_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('list_products')

    return render(request, 'app/pages/Django-Product-API/product-delete-confirm.template.html')