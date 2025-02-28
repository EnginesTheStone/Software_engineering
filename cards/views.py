from django.shortcuts import render, redirect

from .models import myCards, Cart

from rest_framework import generics
from .serialisers import myCardsSeri
from django.contrib.auth.decorators import login_required

# Create your views here.

def home (request):
    return render(request, "home.html")


def buy (request):
    query = request.GET.get('q', '')
    if query:
        cards = myCards.objects.filter(cardname__icontains=query)
    else:
        cards = myCards.objects.all()

        
    return render(request, "buy.html", {"cards": cards, "user":request.user})


def stock (request):
    return render (request, "stock.html")
    
@login_required
def checkout (request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, "checkout.html", {'cart_items': cart_items, 'total_price': total_price})


class myCardsadd(generics.ListCreateAPIView):
    queryset = myCards.objects.all()
    serializer_class = myCardsSeri


@login_required
def add_to_cart(request, product_id):
    product = myCards.objects.get(id=product_id)
    cart_item = Cart.objects.filter(user=request.user, product=product).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        Cart.objects.create(user=request.user, product=product, quantity=1)

    return redirect('buy')

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, "cart.html", {"cart_items": cart_items, "total_price": total_price})

@login_required
def remove_from_cart(request, cart_id):
    cart_item = Cart.objects.get(id=cart_id)
    cart_item.delete()
    return redirect('view_cart')


def purchase_confirmation(request):
    if request.user.is_authenticated:
        Cart.objects.filter(user=request.user).delete()

    return render(request, 'purchase_confirmation.html')

