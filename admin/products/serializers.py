from rest_framework import serializer
from .models import Product

class ProductSerializer(serializer.ModelSerializer):
    class Meta:
        model = product
        fields =  '__all__'