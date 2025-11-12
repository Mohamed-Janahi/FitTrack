from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recovery, Workout
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
            return redirect("index")
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

    #create####################################
class WorkoutCreate(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ["name", "description", "workout_video", "reps", "is_completed"]
    # success_url = "/cats/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#update###########################
class WorkoutUpdate(LoginRequiredMixin, UpdateView):
    model = Workout
    fields = ["name", "description", "workout_video", "reps", "is_completed"]

#delete#####################################
class WorkoutDelete(LoginRequiredMixin, DeleteView):
    model = Workout
    success_url = "/workouts/"


