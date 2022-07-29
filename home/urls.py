from django.contrib import admin
from django.urls import path, include
from home.views import index, loginUser, logoutUser,paramFun

urlpatterns = [
    path('', index, name='index'),
    path('login', loginUser, name='login'),
    path('logout', logoutUser, name='logout'),
    path('check/<int:id>', paramFun, name='paramFun'),
]