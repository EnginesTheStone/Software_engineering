from rest_framework import serializers
from .models import myCards


class myCardsSeri(serializers.ModelSerializer):
     class Meta:
         model=myCards
         fields='__all__'