from pdb import Restart
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from simplynashapi.models import RestaurantPost
from simplynashapi.models import Ambiance
from simplynashapi.models import FoodType
from django.contrib.auth.models import User

class RestaurantPostView(ViewSet):
    def retrieve(self, request, pk):
        restaurantposts = RestaurantPost.objects.get(pk=pk)
        serializer = RestaurantPostSerializer(restaurantposts)
        return Response(serializer.data)
    
    def list(self, request):
        restaurantposts = RestaurantPost.objects.all()
        categories = request.query_params.get('type', None)
        if categories is not None:
            restaurantposts = restaurantposts.filter(categories_id=categories)
        serializer = RestaurantPostSerializer(restaurantposts, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CreateRestaurantPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        restaurantpost = RestaurantPost.objects.get(pk=pk)
        restaurantpost.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        restaurantpost = RestaurantPost.objects.get(pk=pk)
        serializer = CreateRestaurantPostSerializer(restaurantpost, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        restaurantpost.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['post'], detail=False)
    def restaurantpostambiance(self, request):
        ambiance_id = request.data["ambiance"]
        restaurantpost_id = request.data["restaurantpost"]
        ambiance = Ambiance.objects.get(pk=ambiance_id)
        restaurantpost= RestaurantPost.objects.get(pk=restaurantpost_id)
        restaurantpost.ambiance.add(ambiance)
        return Response({'message': 'ambiance added'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=False)
    def removeresturantambiance(self, request):
        ambiance_id = request.data["ambiance"]
        restaurantpost_id = request.data["restaurantpost"]
        ambiance = Ambiance.objects.get(pk=ambiance_id)
        restaurantpost= RestaurantPost.objects.get(pk=restaurantpost_id)
        restaurantpost.ambiance.remove(ambiance)
        return Response({'message': 'ambiance added?'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['post'], detail=False)
    def restaurantpostfoodtype(self, request):
        foodtype_id = request.data["foodtype"]
        restaurantpost_id = request.data["restaurantpost"]
        foodtype = FoodType.objects.get(pk=foodtype_id)
        restaurantpost = RestaurantPost.objects.get(pk=restaurantpost_id)
        restaurantpost.foodtype.add(foodtype)
        return Response({'message': 'foodtype added'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=False)
    def removerestaurantfoodtype(self, request):
        foodtype_id = request.data["foodtype"]
        restaurantpost_id = request.data["restaurantpost"]
        foodtype = FoodType.objects.get(pk=foodtype_id)
        restaurantpost = RestaurantPost.objects.get(pk=restaurantpost_id)
        restaurantpost.foodtype.remove(foodtype)
        return Response({'message': 'foodtype added?'}, status=status.HTTP_201_CREATED)
        
        
class RestaurantPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantPost
        fields = ('id','nashuser','name','publication_date','category','address','parking','price',
                'image_url','description','ambiance','food_type')
        depth = 1
        
class CreateRestaurantPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantPost
        fields = ('id','nashuser','name','publication_date','category','address','parking','price',
                'image_url','description')