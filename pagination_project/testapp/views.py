from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from testapp.pagination import MyPagination,mypagination2,mypagination3
# Create your views here.

class EmployeeListView(generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    search_fields=('eno','ename',)
    ordering_fields=('eno','ename')

