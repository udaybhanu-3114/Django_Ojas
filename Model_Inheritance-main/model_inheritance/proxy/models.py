from django.db import models

# Create your models here.
class table_proxy(models.Model):
    Dept_name =  models.CharField(max_length=20)
    Dept_code = models.CharField(max_length=20)

class table_dubli(table_proxy):
    class Meta:
        proxy = True
