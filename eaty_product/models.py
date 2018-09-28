from django.db import models


class ProductType(models.Model):
    name = models.CharField(max_length=80)
    like = models.IntegerField(default=0,null=True, blank=True)
    dislike = models.IntegerField(default=0,null=True, blank=True)

    def __str__(self):
        #return "%s is the type of product" % self.type_text
        return '{}'.format(self.name)
       

class Product(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cross = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    product_type = models.OneToOneField(ProductType, on_delete=models.CASCADE)

    def product_total(self):
        return self.quantity * self.price

    def __str__(self):
        #return 'Product: %s, Price: %s, Number of crosses: %s, Quantity: %s' % (self.product_type, self.price, self.cross, self.quantity)
        return 'Product: {}, Price: {}€, Number of crosses: {}, Quantity: {}'.format(self.product_type, self.price, self.cross, self.quantity) 