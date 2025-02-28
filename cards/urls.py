from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [

    path("", views.home, name = "home"),
    path("buy/", views.buy, name="buy" ),
    path("checkout/", views.checkout, name = "checkout"),
    
    path('add_to_cart/<int:product_id>/', login_required(views.add_to_cart), name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('purchase_confirmation/', views.purchase_confirmation, name='purchase_confirmation'),

    


]