from django.urls import path
from . import views


urlpatterns=[
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('show', views.show, name='show'),
    path('edit/<int:id>', views.update_ticket, name='update_ticket'),
    path('delete/<int:id>', views.destroy, name='destroy'),
]