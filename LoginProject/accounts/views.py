from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Sum

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
    slp = SLP.objects.all()
    player = User.objects.all()

    total_win = slp.filter(Mode='Win').count()
    total_lose = slp.filter(Mode='lose').count()
    totalLoseWin = total_lose+total_win
    WinRate = total_win/totalLoseWin * 100.0

    TotalSLP = SLP.objects.aggregate(Sum('slp'))['slp__sum']
    context = {'player':player, 'slp':slp,'WinRate':WinRate,'TotalSLP':TotalSLP}

    return render(request,'accounts/dashboard.html',context)

def sSLP(request):
    slp = SLP.objects.all()

    return render(request,'accounts/SLP.html',{'SLP':slp})