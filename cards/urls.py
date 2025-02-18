from django.urls import path
from . import views

urlpatterns = [

    path("home/", views.index, name = "index"),
    path("buy/", views.buy, name="buy" ),
    path("sell/", views.sell, name = "sell"),
    path("stock/", views.stock, name = "stock"),
    path("signup/", views.signup, name = "signup"),
    path("checkout/", views.checkout, name = "checkout"),
    path("api/", views.myCardsadd.as_view(), name = "cards_add"),

]