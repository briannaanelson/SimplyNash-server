from django.db import models

class Ambiance(models.Model):
    label = models.CharField(max_length=60)