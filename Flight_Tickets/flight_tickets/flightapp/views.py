from django.shortcuts import render,redirect, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import Ticket_forms
from .models import TicketBookModel
from django.contrib import messages
from django.views import View
from .forms import SignupForm
from datetime import datetime, timedelta

class home(View):
    def post(self,request):
        fm = Ticket_forms(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            flight_name = fm.cleaned_data['flight_name']
            ticket_no = fm.cleaned_data['ticket_no']
            no_of_tickets = fm.cleaned_data['no_of_tickets']
            request.session['name'] = name
            request.session['flight_name'] = flight_name
            request.session.set_expiry(600)
            response = render(request, 'show.html')
            response.set_signed_cookie('flight_name', flight_name, salt='flight_name',
                                       expires=datetime.utcnow() + timedelta(days=2))
            obj = TicketBookModel(name=name,email=email,flight_name=flight_name,ticket_no=ticket_no,no_of_tickets=no_of_tickets)
            obj.save()
            det = TicketBookModel.objects.all()
            return render(request, 'show.html', {'form': fm, 'details': det})
    def get(self,request):
        fm = Ticket_forms()
        det = TicketBookModel.objects.all()
        return render(request,'show.html',{'form':fm,'details':det})

class destroy(View):
    def get(self,request,id):
        stu = TicketBookModel.objects.get(pk=id)
        stu.delete()
        return redirect('/')

class update_ticket(View):
    def post(self,request,id):
        stu = TicketBookModel.objects.get(pk=id)
        form = Ticket_forms(request.POST, instance=stu)
        if form.is_valid():
            messages.success(request, 'successfully updated!')
            form.save()
            return redirect('/')
    def get(self,request,id):
        stu = TicketBookModel.objects.get(pk=id)
        form = Ticket_forms(instance=stu)
        return render(request, 'show.html', {'form': form})

#--------------------

class signup(View):
    def post(self,request):
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Succesfully')
            fm.save()
        return render(request, 'signup.html', {'form': fm})
    def get(self,request):
        fm = SignupForm()
        return render(request, 'signup.html', {'form': fm})


class user_login(View):
   ''' if not request.user.is_authenticated:'''
   def post(self,request):
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/home')
        return render(request, 'user_login.html', {'form': fm})
   def get(self,request):
        fm = AuthenticationForm()
        return render(request, 'user_login.html', {'form': fm})


class first_page(View):
    def get(self,request):
        return render(request,'first_page.html')

class user_logout(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/login')

#--------------Cookies and session

def getsession(request):
    name = request.session['name']
    flight_name = request.session['flight_name']
    # name = request.session.get('name', default = 'Guest')
    # keys = request.session.keys()
    # key = request.session.items()
    # age = request.session.setdefault('age', '36')
    request.session.modified = True
    context = {'name': name, 'flight_name': flight_name}
    return render(request, 'getsession.html',context )

def delsession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'delsession.html')

def getcookie(request):
    # name = request.COOKIES.get('name','Guest')
    flight_name = request.get_signed_cookie('flight_name', default = 'Guest',salt = 'flight_name')
    # name = request.COOKIES['name']
    return render(request, 'getcookie.html', {'flight_name':flight_name})

def delcookie(request):
    response = render(request, 'delcookie.html')
    response.delete_cookie('flight_name')
    return response
