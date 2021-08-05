from django.db import models

# Create your models here.

class Dept(models.Model):
    Dept_name =  models.CharField(max_length=20)
    Dept_code = models.CharField(max_length=20)


class Student(Dept):
    stu_name = models.CharField(max_length=20)
    age = models.IntegerField(default=16)

