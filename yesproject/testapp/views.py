from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
# Create your views here.
class Mypagination(PageNumberPagination):
    page_size=15
    page_query_param='mypage'
    page_size_query_param='num'
    max_page_size=15
    last_page_strings=('last',)

class mypagination2(CursorPagination):
    ordering='esal'
    page_size=15




class Home_View(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    # pagination_class=mypagination2
    search_fields=('ename','esal',)


    def get_queryset(self):
        qs=Employee.objects.all()

        name=self.request.GET.get('ename')
        if name is not None:
            qs=qs.filter(ename__icontains=name)
        return qs