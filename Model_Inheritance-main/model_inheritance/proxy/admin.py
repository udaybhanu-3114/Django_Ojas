from django.contrib import admin
from .models import table_proxy,table_dubli
# Register your models here.
@admin.register(table_proxy)
class AdminDept(admin.ModelAdmin):
    list_display = ['Dept_name','Dept_code']

@admin.register(table_dubli)
class AdminDept(admin.ModelAdmin):
    list_display = ['Dept_name','Dept_code']