from rest_framework import serializers
from eaty_product.models import ProductType, Product

class ProductTypeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the ProductType model """
    class Meta:
        model = ProductType
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Product model """
    product_type=ProductTypeSerializer()
    
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ("product_type","quantity","cross","price")

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        product_data = validated_data.pop('product_type')
        product_type = ProductTypeSerializer.create(ProductTypeSerializer(), validated_data=product_data)
        theproduct, created = Product.objects.update_or_create(product_type=product_type,
                            quantity=validated_data.pop('quantity'),
                            price=validated_data.pop('price'))
        return theproduct


    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.price = validated_data.get('price', instance.price)

        instance.save()

        product_type = validated_data.get('product_type')

        for produs in product_type:
            produs_id = produs.get('id', None)
            if produs_id:
                inv_produs = Product.objects.get(id=produs_id, invoice=instance)
                inv_produs.quantity = produs.get('quantity', inv_produs.quantity)
                inv_produs.price = produs.get('price', inv_produs.price)
                inv_produs.save()
            else:
                Product.objects.create(account=instance, **produs)

        return instance