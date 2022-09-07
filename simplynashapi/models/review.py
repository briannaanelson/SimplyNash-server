from django.db import models
from simplynashapi.models import restaurant_post
from simplynashapi.models.restaurant_post import RestaurantPost
from simplynashapi.models.nash_user import NashUser
from simplynashapi.models.rating import Rating

class Review(models.Model):
    restaurant_post = models.ForeignKey(RestaurantPost, on_delete=models.CASCADE)
    user = models.ForeignKey(NashUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    created_on = models.DateField()
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)