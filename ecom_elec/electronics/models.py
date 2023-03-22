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

