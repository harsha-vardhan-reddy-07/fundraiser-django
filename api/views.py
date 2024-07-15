from django.shortcuts import render


def landing(request):
    return render(request, 'landing.html')


def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')

def newFundraiser(request):
    return render(request, 'newfunding.html')

def myFundraisers(request):
    return render(request, 'myfundraisers.html')

def fundraiser(request, id):
    return render(request, 'fundraiserdetails.html')

def updateFundraiser(request, id):
    return render(request, 'updatefunding.html')


def admin(request):
    return render(request, 'admin.html')

def allUsers(request):
    return render(request, 'allusers.html')

def allFundraisers(request):
    return render(request, 'allfundraisers.html')

def allDonations(request):
    return render(request, 'alldonations.html')