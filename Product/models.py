from django.db import models


class Type(models.Model):
    type_text = models.CharField(max_length=30)
    def __str__(self):
        #return "%s is the type of product" % self.type_text
        return self.type_text
       

class Product(models.Model):
    prixachat_number = models.IntegerField()
    croix_number = models.IntegerField()
    quantity_number = models.IntegerField(default=0)
    produs = models.ForeignKey(Type, on_delete=models.CASCADE)

   
    def __str__(self):
        return 'Product: %s, Prix Achat: %s, Croix number: %s, Quantity: %s' % (self.produs, self.prixachat_number, self.croix_number, self.quantity_number)
    