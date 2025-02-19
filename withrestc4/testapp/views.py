from django.shortcuts import render
from testapp.models import Employee
from rest_framework.viewsets import ModelViewSet
from testapp.serailzers import EmployeeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from testapp.permissions import IsReadOnly,IsGetOrPatch,SunnyPermissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from testapp.authentication import CustomAuthentication,CustomAuthentication2
# Create your views here.
 
class EmployeeCURDCBV(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    # authentication_classes=[JWTAuthentication,]
    # permission_classes=[IsAuthenticated,]
    authentication_classes=[CustomAuthentication2,]
    permission_classes=[IsAuthenticated,]