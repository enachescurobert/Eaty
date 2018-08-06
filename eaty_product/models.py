from django.db import models


class ProductType(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        #return "%s is the type of product" % self.type_text
        return self.name
       

class Product(models.Model):
    price = models.FloatField()
    cross = models.FloatField()
    quantity = models.IntegerField(default=0)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

   
    def __str__(self):
        #return 'Product: %s, Price: %s, Number of crosses: %s, Quantity: %s' % (self.product_type, self.price, self.cross, self.quantity)
        return 'Product: {},Price: {}, Number of crosses: {}, Quantity: {}'.format(self.product_type, self.price, self.cross, self.quantity) 