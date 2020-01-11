from django.db import models

# Create your models here.
class authentication(models.Model):
    userName=models.CharField(max_length=100)
    password=models.CharField(max_length=8)
