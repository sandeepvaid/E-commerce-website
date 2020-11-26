from django.db import models

# Create your models here.
class products(models.Model):

    def __str__(self):
        return self.title
    
    title= models.CharField(max_length=200)
    price =models.FloatField()
    discount_price=models.FloatField()
    desc = models.TextField()
    image= models.CharField(max_length=500)
    category = models.CharField(max_length=200 , default="random")

class Order(models.Model):

    def __str__(self):
        return self.name

    item = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    state = models.CharField(max_length=1000)
    zipcode = models.CharField(max_length=1000)
    total =models.CharField(max_length=200)

