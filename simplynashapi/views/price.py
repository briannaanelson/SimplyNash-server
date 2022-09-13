from dataclasses import fields
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplynashapi.models import Price, price

class PriceTypeView(ViewSet):
    def retrieve(self, request, pk):
        try:
            price = Price.objects.get(pk = pk)
            serializer = PriceSerializer(price)
            return Response(serializer.data)
        except Price.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        prices = Price.objects.all()
        serializer = PriceSerializer(prices, many=True)
        return Response(serializer.data)
            


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('id', 'label')