from django.db import models

# Create your models here.
class ProductInfo(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    details = models.CharField(max_length=255)
    reviews = models.IntegerField()
    stars = models.IntegerField()
    image = models.ImageField(upload_to='')

class ShopProducts(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stars = models.IntegerField()
    size = models.CharField(max_length=255)
    image = models.ImageField(upload_to='')

class Cart(models.Model):
    cartCount = models.IntegerField()