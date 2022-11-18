from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=400)
    logo = models.CharField(max_length=300)
    slug = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=400)
    slug = models.CharField(max_length=400)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Slider Backend
class Slider(models.Model):
    name = models.CharField(max_length=400)
    image = models.ImageField(upload_to='media')
    url = models.URLField(max_length=400)


# Ad backend
class Ad(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    rank = models.IntegerField()

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=400)
    image = models.ImageField(upload_to='media')
    slug = models.CharField(max_length=400)

    def __str__(self):
        return self.name


STOCK = (('in stock','in stock'),('out of stock'),('out of stock'))
LABELS = (('hot','hot'),('new','new'),('sale','sale'))

class Product(models.Model):
    name = models.CharField(max_length=400)
    slug = models.CharField(max_length=400)
    image = models.ImageField(upload_to='media')
    price = models.IntegerField(max_length=300)
    discounted_price = models.IntegerField(default = 0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    stock = models.CharField(max_length=100, choices='')
    labels = models.CharField(max_length=100,choices = LABELS)

    def __str__(self):
        return self.name