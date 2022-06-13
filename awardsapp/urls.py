from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('navbar/', views.navbar, name='navbar'),
    # path('login/', views.login, name='login'),
    path('login/', views.loginPage, name="login"),  
    path('register/', views.register, name='register'),
   
]