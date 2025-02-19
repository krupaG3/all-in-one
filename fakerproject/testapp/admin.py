from django.contrib import admin
from testapp.models import *
# Register your models here.

class Hyd_Jobs_Admin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']



admin.site.register(Hyd_Jobs_Model,Hyd_Jobs_Admin)