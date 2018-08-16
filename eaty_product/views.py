from eaty_product.models import ProductType, Product
from eaty_product.serializers import ProductSerializer,ProductTypeSerializer
from rest_framework import generics

class ProductTypeList(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer