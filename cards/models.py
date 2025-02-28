from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class myCards(models.Model):

    class  Meta:
        verbose_name_plural = "myCards"

    cardname = models.CharField(max_length = 100)
    cardprice = models.DecimalField(max_digits = 10, decimal_places = 2)
    stock = models.IntegerField()
    cardimage = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.cardname
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(myCards, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
            return f"{self.product.cardname} (x{self.quantity})"
        
    def get_total_price(self):
            return self.quantity * self.product.cardprice

