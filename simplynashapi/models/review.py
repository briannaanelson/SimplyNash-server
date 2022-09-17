from django.db import models
from django.contrib.auth.models import User
from simplynashapi.models.restaurant_post import RestaurantPost
from simplynashapi.models.rating import Rating

class Review(models.Model):
    restaurant_post = models.ForeignKey(RestaurantPost, on_delete=models.CASCADE)
    nashuser = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    created_on = models.DateField()
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)