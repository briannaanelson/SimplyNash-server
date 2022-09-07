from django.db import models
from simplynashapi.models.nash_user import NashUser
from simplynashapi.models.ambiance import Ambiance
from simplynashapi.models.food_type import FoodType
from simplynashapi.models.price import Price

class RestaurantPost(models.Model):
    user = models.ForeignKey(NashUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    publication_date = models.DateField()
    address = models.CharField(max_length=200)
    parking = models.IntegerField()
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=500, default=None)
    description = models.CharField(max_length=500)
    ambiance = models.ManyToManyField(Ambiance, through="RestaurantAmbiance", related_name="post")
    food_type = models.ManyToManyField(FoodType, through="RestaurantFoodType", related_name="post")
    
    