from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Recovery, Workout, Profile
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import requests


def myApi(request):
    url = "https://www.exercisedb.dev/api/v1/exercises"
    response = requests.get(url)
    exercises = response.json()
    return render(request, "Api.html", {"exercises": exercises})


@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, "users/profile.html", {"profile": profile})


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ["bio", "image"]
    template_name = "users/profile_form.html"

    def get_object(self):
        return self.request.user.profile

    def get_success_url(self):
        return reverse("users-profile")


# Create your views here.
def home(request):
    return render(request, "home.html")


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            error_message = "Invalid Sign-up please try again later."
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)


@login_required
def workouts_index(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, "workouts/index.html", {"workouts": workouts})


@login_required
def workouts_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    return render(request, "workouts/detail.html", {"workout": workout})

    # create####################################


class WorkoutCreate(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ["name", "description", "workout_video", "reps", "is_completed"]
    # success_url = "/cats/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# update###########################
class WorkoutUpdate(LoginRequiredMixin, UpdateView):
    model = Workout
    fields = ["name", "description", "workout_video", "reps", "is_completed"]


# delete#####################################
class WorkoutDelete(LoginRequiredMixin, DeleteView):
    model = Workout
    success_url = "/workouts/"


class RecoveryCreate(LoginRequiredMixin, CreateView):
    model = Recovery
    fields = ["sleep_time", "food"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RecoveryUpdate(LoginRequiredMixin, UpdateView):
    model = Recovery
    fields = ["sleep_time", "food"]


class RecoveryDelete(LoginRequiredMixin, DeleteView):
    model = Recovery
    success_url = "/recovery/"


@login_required
def recoveries_index(request):
    recoveries = Recovery.objects.filter(user=request.user)
    return render(request, "recoveries/recovery_list.html", {"recoveries": recoveries})


@login_required
def recoveries_detail(request, recovery_id):
    recovery = Recovery.objects.get(id=recovery_id)
    return render(request, "recoveries/recovery_detail.html", {"recovery": recovery})
