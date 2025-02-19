from django.contrib import admin
from testapp.models import Employee
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display=[
        field.name for field in Employee._meta.get_fields()
    ]

admin.site.register(Employee,EmployeeAdmin)