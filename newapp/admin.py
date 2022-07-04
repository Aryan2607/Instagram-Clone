from django.contrib import admin
from newapp.models import Employee
from newapp.models import student
# Register your models here.
#admin.site.register(Employee)
# admin.site.register(student)


class studentAdmin(admin.ModelAdmin):
    list_display=["Name","Email","Roll_no","Address"]
    #filter_horizontal=('info',)
admin.site.register(student, studentAdmin)
class EmployeeAdmin(admin.ModelAdmin):
    filter_horizontal=('info',)
admin.site.register(Employee, EmployeeAdmin)