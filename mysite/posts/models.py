from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    category = models.CharField(max_length=100)
    def __str__(self):
      return self.title