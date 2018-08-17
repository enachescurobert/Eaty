from eaty_product.models import ProductType, Product
from eaty_product.serializers import ProductSerializer,ProductTypeSerializer
from rest_framework import generics

from django.shortcuts import render


class ProductTypeList(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

def index(request):
    product_name = ProductType.objects.all()
    return render(request,"app/components/product-type/product-type.template.html", {'product_name':product_name})
