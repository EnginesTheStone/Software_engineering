from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request, "home.html")


def buy (request):
    return render(request, "buy.html")

def sell (request):
    return render(request, "sell.html")

def stock (request):
    return render(request, "stock.html")
