from django.contrib import admin

# Register your models here.
from testapp.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display=[
        field.name for field in Employee._meta.get_fields()
    ]


admin.site.register(Employee,EmployeeAdmin)