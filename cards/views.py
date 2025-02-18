from django.shortcuts import render

from .models import myCards
# from .form import myBooksForm
# from .form import ContactForm

from rest_framework import generics
from .serialisers import myCardsSeri

# Create your views here.

def index (request):
    return render(request, "home.html")


def buy (request):
    return render(request, "buy.html")

def sell (request):
    return render(request, "sell.html")


def stock (request):
    return render (request, "stock.html")
    

def checkout (request):
    return render(request, "checkout.html")

def signup (request):
    return render(request, "signup.html")

class myCardsadd(generics.ListCreateAPIView):
    queryset = myCards.objects.all()
    serializer_class = myCardsSeri


