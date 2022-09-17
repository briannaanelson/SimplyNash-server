from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from simplynashapi.models.category import Category
from simplynashapi.models.ambiance import Ambiance
from simplynashapi.models.food_type import FoodType
from simplynashapi.models.price import Price

class RestaurantPost(models.Model):
    nashuser = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    publication_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    parking = models.IntegerField()
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=500, default=None)
    description = models.CharField(max_length=500)
    ambiance = models.ManyToManyField(Ambiance, related_name="post")
    food_type = models.ManyToManyField(FoodType, related_name="post")
    
    