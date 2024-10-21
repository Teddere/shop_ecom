from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class LastProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)