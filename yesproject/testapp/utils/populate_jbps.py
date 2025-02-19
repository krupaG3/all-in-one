import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','yesproject.settings')

django.setup()

import random
from testapp.models import Employee
from faker import Faker

faker=Faker()


def wish(n):
    for i in range(n):
        feno=random.randint(1,100)
        fename=faker.name()
        fesal=random.randint(30000,50000)
        feaddr=faker.address()

        records=Employee.objects.create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)

wish(50)