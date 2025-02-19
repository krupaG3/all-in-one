from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=50)
    ceo=models.CharField(max_length=50)
    location=models.CharField(max_length=50)


