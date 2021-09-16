from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request,'accounts/BSproject.html')

def contact(request):
    return HttpResponse('home page')

def login(request):
    return render(request, 'accounts/login.html')  

def signup(request):
    return render(request,'accounts/signup.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def sSLP(request):
    slp = SLP.objects.all()

    return render(request,'accounts/SLP.html',{'SLP':slp})