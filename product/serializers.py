from rest_framework import serializers
from .models import Product,Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id','name','description','price','sale_price','stock','get_image','get_thumbnail','get_absolute_url'
        )