from django.db import models 

class Rating(models.Model):
    score = models.IntegerField()