from django.shortcuts import render

# Create your views here.

def facebook(request):
	msg = "CLIENT IS ACESSING FACEBOOK"
	my_dict = {'msg':msg}

	return render(request,'chatapp/fb.html',context=my_dict)

def whatsapp(request):
	msg = "CLIENT IS ACCESSING WHATSAPP"
	my_dict = {'msg':msg}

	return render(request,'chatapp/wtsup.html',context=my_dict)

def instagram(request):
	msg = "CLIENT IS ACCESSING INSTAGRAM"
	my_dict = {'msg':msg}

	return render(request,'chatapp/insta.html',context=my_dict)