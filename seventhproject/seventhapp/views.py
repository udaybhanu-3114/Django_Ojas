from django.shortcuts import render

# Create your views here.

def deposit(request):
	msg = "CLIENT IS DEPOSITING THE AMOUNT"
	my_dict = {'msg':msg}

	return render(request,'seventhapp/display.html',context=my_dict)

def balance(request):
	msg = "CLIENT IS CHECKING THE BALANCE AMOUNT"
	my_dict = {'msg':msg}

	return render(request,'seventhapp/display.html',context=my_dict)

def withdraw(request):
	msg = "CLIENT IS WITHDRAWING THE AMOUNT"
	my_dict = {'msg':msg}

	return render(request,'seventhapp/display.html',context=my_dict)