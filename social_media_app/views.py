from django.shortcuts import render,redirect


# Create your views here.


def home(request):
    return render(request, "home.html")

def dash(request):
    return render(request, 'dash.html')

def user_dash(request):
    return render(request, 'user_dash.html')

