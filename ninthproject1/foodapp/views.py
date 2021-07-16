from django.shortcuts import render

# Create your views here.

def swiggy(request):
	msg = "CLIENT IS ORDERING FOOD THRU SWIGGY"
	my_dict = {'msg':msg}

	return render(request,'foodapp/swiggy.html',context=my_dict)

def zomato(request):
	msg = "CLIENT IS ORDERING FOOD THRU ZOMATO"
	my_dict = {'msg':msg}

	return render(request,'foodapp/zomato.html',context=my_dict)

