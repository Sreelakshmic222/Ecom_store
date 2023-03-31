from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Elec(models.Model):
    name = models.CharField(max_length=200)
    Company = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.FloatField(null=True,blank=True)
    image_url=models.CharField(max_length=2083,blank=True)
    follow_company=models.CharField(max_length=2083,blank=True)
    stock_availability = models.BooleanField()

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Elec, max_length=200, null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __str(self):
        return self.product.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Elec, on_delete=models.CASCADE)
    image_url = models.CharField(max_length = 2083, default=False)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Elec, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    stock_availability = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.CharField(max_length = 2083, default=False)