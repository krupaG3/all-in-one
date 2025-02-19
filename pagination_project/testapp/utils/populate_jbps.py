import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','pagination_project.settings')

django.setup()

from testapp.models import Employee
from random import *
from faker import Faker

faker=Faker()
def populate(n):
    for i in range(n):
        feno = randint(100, 200)
        fename = faker.name()
        fesal = randint(10000, 20000)
        feaddr = faker.city()
        
        # Create and save the employee record
        emp_record=Employee.objects.create(eno=feno, ename=fename, esal=fesal, eaddr=feaddr)

# Populate the database with 120 records
populate(120)
