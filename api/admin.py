from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['name','age','gender','department','salary']
	list_filter = ('gender','department')