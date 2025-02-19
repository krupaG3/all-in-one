import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','fakerproject.settings')

django.setup()

from random import *
from testapp.models import *
from faker import Faker

fake=Faker()

def phonenumbgen():
    a=randint(7,9)
    output=''+str(a)
    for i in range(9):
        output+=str(randint(0,9))
    return int(output)

def populate(n):
    for _ in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Developer','Tester','HR','CEO','Clerk','Chef'))
        feligibility=fake.random_element(elements=('B.SC','M.SC.','BCA','IAS'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbgen()
        hydjobs=Hyd_Jobs_Model.objects.create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,
                                              address=faddress,email=femail,phonenumber=fphonenumber)
populate(50)
