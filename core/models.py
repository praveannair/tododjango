from django.db import models

# Create your models here.

class todo(models.Model):
    task=models.CharField(max_length=50)

class product(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    desc=models.CharField(max_length=200)
    url=models.CharField(max_length=200)
    