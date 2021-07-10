from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome_django(request):

	s1 = "<center><h1>Hello Abcians</h1></center>"

	s2 = "<center><h1 style = 'color:red'>Welcome to Django Framework</h1></center>"

	s3 = (s1,s2)

	return HttpResponse(s3)


