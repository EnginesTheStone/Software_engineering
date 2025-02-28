from .models import Cart
from django.db.models import Sum

def cart_count(request):

    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0 

    else:
        cart_count = 0

    return {'cart_count': cart_count}