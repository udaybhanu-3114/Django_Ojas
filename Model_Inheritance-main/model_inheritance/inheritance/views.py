from django.shortcuts import render
from .models import StudentDetail
# Create your views here.
def home(request):
    obj = StudentDetail.objects.all()
    return render(request,'home.html',{'obj':obj})

