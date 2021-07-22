from django.db import models

# Create your models here.
class student(models.Model):
    sid = models.IntegerField(primary_key=True)
    sname = models.CharField(max_length=100)
    semail = models.EmailField(max_length=100)
    spass = models.CharField(max_length=100)
    comment = models.CharField(max_length=100,default='Not available')

    def __str__(self):
        return str(self.sname)
