from dataclasses import fields
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from simplynashapi.models import Price

class PriceTypeView(ViewSet):
    def retrieve(self, request, pk):
        prices = Price.objects.get(pk = pk)
        serializer = PriceSerializer(prices)
        return Response(serializer.data)

        
    def list(self, request):
        prices = Price.objects.all()
        serializer = PriceSerializer(prices, many=True)
        return Response(serializer.data)
            


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('id', 'label')