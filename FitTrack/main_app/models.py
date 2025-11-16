from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="", upload_to="main_app/static/profile_images/")
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    workout_video = models.URLField()
    reps = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("workouts_detail", kwargs={"workout_id": self.id})


class Recovery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sleep_time = models.IntegerField()
    food = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    score = models.IntegerField(default=0)

    # create a function
    def final_result(self):
        # calculation

        sleeping_calculation = self.sleep_time * 12.5
        meals_calculation = self.food * 20

        return int((sleeping_calculation + meals_calculation) / 2)

    # saving the score in the DB
    def save(self, *args, **kwargs):
        self.score = self.final_result()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Recovery on {self.date}"

    def get_absolute_url(self):
        return reverse("recovery_detail", kwargs={"recovery_id": self.id})


# for the super part
# telling django call your function to save it to the database. (since we create a function name save and the django have also a function name save we are telling the app well i gave you the values to save now your turn to use (your save function) and save it in the database)
