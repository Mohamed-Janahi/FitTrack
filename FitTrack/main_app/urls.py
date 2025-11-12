from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/signup/", views.signup, name="signup"),

####workout######################################

    path("workouts/", views.workouts_index, name="workouts_index"),
    path("workouts/<int:workout_id>/", views.workouts_detail, name="workouts_detail"),
    path("workouts/create/", views.WorkoutCreate.as_view(), name="workouts_create"),
    path("workouts/<int:pk>/update/", views.WorkoutUpdate.as_view(), name="workouts_update"),
    path("workouts/<int:pk>/delete/", views.WorkoutDelete.as_view(), name="workouts_delete"),
]

