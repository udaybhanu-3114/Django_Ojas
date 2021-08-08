"""movies_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from flightapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home.as_view(), name = 'home'),
    path('signup',views.signup.as_view(), name='signup'),
    path('login',views.user_login.as_view(),name='login'),
    path('',views.first_page.as_view(),name='first_page'),
    path('logout', views.user_logout.as_view(),name='logout'),
    path('edit/<int:id>', views.update_ticket.as_view(), name = 'update_ticket'),
    path('delete/<int:id>', views.destroy.as_view(), name = 'destroy'),
    path('get_sess', views.getsession, name = 'get'),
    path('del_sess', views.delsession, name = 'del'),
    path('del_coo', views.delcookie, name = 'del'),
    path('get_coo', views.getcookie, name = 'get'),
]
