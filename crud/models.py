from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    document = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    User = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    
    def __str__(self):
        return "%s - %s %s" % (self.id,self.first_name, self.last_name)

class Bill(models.Model):
    
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)
    company_name = models.CharField(max_length=50)
    nit = models.PositiveIntegerField()
    code = models.PositiveIntegerField()
    def __str__(self):
        return "%s - %s" % (self.id, self.company_name)

class Product(models.Model):
    
    name = models.CharField(max_length=50)
    description = models.TextField()
    attribute_4 = models.TextField()
    def __str__(self):
        return "%s - %s" % (self.id, self.name)


class Bills_Product(models.Model):
    
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id