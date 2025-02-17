from django.db import models

# Create your models here.
class myCards(models.Model):

    class  Meta:
        verbose_name_plural = "myCards"

    cardName = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 50)
    cardType = models.CharField(max_length = 50)
    description = models.CharField(max_length = 255)
    manaCost = models.CharField(max_length = 10)
    cardPrice = models.DecimalField(max_digits = 10, decimal_places = 2)
    cardGuild = models.CharField(max_length = 10)
    cardSet = models.CharField(max_length = 10)
    stock = models.IntegerField()

def __str__(self):
    return f"CardName:{self.cardName}"
