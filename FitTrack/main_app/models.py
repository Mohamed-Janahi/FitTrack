from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    workout_video = 
