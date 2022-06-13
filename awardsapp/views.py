from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'base.html')


def navbar(request):
    return render(request, 'navbar.html')


def login_user(request):
    return render(request, 'login.html')