from django.contrib import admin
from .models import Dept, Student
# Register your models here.
@admin.register(Dept)
class AdminDept(admin.ModelAdmin):
    list_display = ['Dept_name','Dept_code']

@admin.register(Student)
class AdminDept(admin.ModelAdmin):
    list_display = ['stu_name','age']