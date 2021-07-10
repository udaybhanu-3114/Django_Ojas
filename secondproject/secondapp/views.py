from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def greeting_django(request):
	s1 = "<center><h1>Hello: Good Morning</h1></center>"
	time = datetime.now().time()
	s2 = "<center><h1>The Server Time is:"+str(time)+"</h1></center>"
	output = (s1,s2)
	return HttpResponse(output)

