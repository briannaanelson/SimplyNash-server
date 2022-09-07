from django.db import models

class Price(models.Model):
    label= models.CharField(max_length=20)