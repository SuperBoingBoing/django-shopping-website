from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Snack(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Movie(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="myapp/files/covers")

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Phone, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def total_cost(self):
        return self.quantity * self.product.price