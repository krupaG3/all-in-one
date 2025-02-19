from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    marks=models.IntegerField()
    class Meta:
        abstract=True
    



class Teacher(ContactInfo):
    salary=models.IntegerField()
    location=models.CharField(max_length=140)

class Attender(ContactInfo):
    work=models.CharField(max_length=33)
    personality=models.CharField(max_length=44)


class ContactInfo1(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    marks=models.IntegerField()
    


class Teacher1(ContactInfo1):
    salary=models.IntegerField()
    location=models.CharField(max_length=140)

class Attender1(ContactInfo1):
    work=models.CharField(max_length=33)
    personality=models.CharField(max_length=44)

