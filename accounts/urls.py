from django.contrib import admin
from django.urls import path,include
from .views import UserRegistraion #,UserLogin

urlpatterns = [
    path('register/', UserRegistraion.as_view(), name='register'),
    
]
#