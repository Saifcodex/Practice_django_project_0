from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    description = models.CharField(max_length=1000, default="Write the description of the Product")
    def __str__(self):
     return self.Name