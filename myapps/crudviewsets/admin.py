from django.contrib import admin
from .models import Employee


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)
admin.site.site_header = 'Haritha Computers & Technology'
