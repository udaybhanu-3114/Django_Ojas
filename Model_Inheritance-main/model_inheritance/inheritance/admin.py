from django.contrib import admin
from .models import StudentDetail
# Register your models here.
@admin.register(StudentDetail)
class AdminStudentDetails(admin.ModelAdmin):
    list_display = ['st_id','name','age','place']

