from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
   # path('register',views.register,name="register"),
    path('submit_form',views.submit_form,name="submit_form"),
    #path('myprofile',views.myprofile,name="myprofile"),
    #path('printinv/',views.printinv,name="printinv"),
    #path('forgot-password',views.forgot_password,name="forgot-password"),
    #path('reset-password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
]
