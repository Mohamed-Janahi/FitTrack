from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    workout_video = models.URLField()
    reps = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("workouts_detail", kwargs={"workout_id": self.id})

class Recovery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sleep_time = models.TimeField()
    food = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recovery_detail", kwargs={"recovery_id": self.id})
