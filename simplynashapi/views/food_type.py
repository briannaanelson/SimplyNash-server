"""View Module for handling request about food types"""
from dataclasses import fields
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response 
from rest_framework import serializers, status
from simplynashapi.models import FoodType, food_type


class FoodTypeView(ViewSet):
    """Simply Nash food types view"""
    
    def retrieve(self, request, pk):
        try: 
            food_type = FoodType.objects.get(pk=pk)
            serializer =FoodTypeSerializer(food_type)
            return Response(serializer.data)
        except FoodType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
            
    
    def list(self, request):
        food_types = FoodType.objects.all()
        serializer = FoodTypeSerializer(food_types, many=True)
        return Response(serializer.data)




class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = ('id', 'label')