from django.db import models

# Create your models here.
class Prod(models.Model):
    name = models.CharField(max_length=64)
    info = models.TextField()
    price= models.IntegerField()

class Exemple(models.Model):
    name=models.CharField(max_length=30)
    url =models.CharField(max_length=32)
    page = models.ImageField(upload_to='static/')
    info = models.TextField(default='none')

class Blog(models.Model):
    types=models.CharField(max_length=25)
    name=models.CharField(max_length=30)
    cont= models.TextField()

    comm = models.CharField(max_length=85)
    count=models.IntegerField()

