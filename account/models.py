from django.db import models

class Users (models.Model):
    login = models.CharField(max_length=50 , unique=True)
    password = models.CharField(max_length=35 )
    balanse = models.IntegerField(default=0)


