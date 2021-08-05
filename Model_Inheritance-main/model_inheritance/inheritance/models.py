from django.db import models

# Create your models here.
class ABC(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    class Meta:
        abstract = True

class StudentDetail(ABC):
    st_id = models.CharField(max_length=10)
    place = models.CharField(max_length=50)
