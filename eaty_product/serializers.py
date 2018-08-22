from rest_framework import serializers
from eaty_product.models import ProductType, Product

class ProductTypeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the ProductType model """
    class Meta:
        model = ProductType
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Product model """
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ("product_type","quantity","cross","price")