from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField()
    price  = models.IntegerField()
