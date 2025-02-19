from django.contrib import admin
from testapp.models import Company_Model
# Register your models here.

class Company_Admin(admin.ModelAdmin):
    list_display=['name','ceo','location']


admin.site.register(Company,Company_Admin)