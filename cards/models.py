from django.db import models


# Create your models here.
class myCards(models.Model):

    class  Meta:
        verbose_name_plural = "myCards"

    card_id = models.CharField(max_length=10)
    cardName = models.CharField(max_length = 100)
    cardPrice = models.DecimalField(max_digits = 10, decimal_places = 2)
    stock = models.IntegerField()

    def __str__(self):
        return self.cardName

