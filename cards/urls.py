from django.urls import path, include
from . import views
from django.shortcuts import redirect

def redirect_to_home(request):
    return redirect ('/cards/')




urlpatterns = [
    #URL links#
    path('', redirect_to_home),
    path("cards/", include('cards.urls')),#views.home, name = "home"#),
    path("buy/", views.buy, name="buy" ),
    path("checkout/", views.checkout, name = "checkout"),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('purchase_confirmation/', views.purchase_confirmation, name='purchase_confirmation'),

    


]