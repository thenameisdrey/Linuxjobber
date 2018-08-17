from django.shortcuts import render

def index(request):
    return render(request, 'home/linuxjobber.html')

def login(request):
    return render(request, 'home/login.html')

def signup(request):
    return render(request, 'home/signup.html')

def selfstudy(request):
    return render(request, 'home/selfstudy.html')
