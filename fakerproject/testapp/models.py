from django.db import models

# Create your models here.
class Hyd_Jobs_Model(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=40)
    title=models.CharField(max_length=40)
    eligibility=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    phonenumber=models.IntegerField()

    