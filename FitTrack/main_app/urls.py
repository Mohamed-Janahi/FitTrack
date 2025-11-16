from django.urls import path, include
from . import views
from .views import profile

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/signup/", views.signup, name="signup"),

####workout######################################

    path("workouts/", views.workouts_index, name="workouts_index"),
    path("workouts/<int:workout_id>/", views.workouts_detail, name="workouts_detail"),
    path("workouts/create/", views.WorkoutCreate.as_view(), name="workouts_create"),
    path("workouts/<int:pk>/update/", views.WorkoutUpdate.as_view(), name="workouts_update"),
    path("workouts/<int:pk>/delete/", views.WorkoutDelete.as_view(), name="workouts_delete"),

#recovery#######################
    path("recovery/", views.recoveries_index, name="recovery_index"),
    path("recovery/<int:recovery_id>/", views.recoveries_detail, name="recovery_detail"),
    path("recovery/create/", views.RecoveryCreate.as_view(), name="recovery_create"),
    path("recovery/<int:pk>/update/", views.RecoveryUpdate.as_view(), name="recovery_update"),
    path("recovery/<int:pk>/delete/", views.RecoveryDelete.as_view(), name="recovery_delete"),
    path('profile/', views.profile, name='users-profile'),
    path('profile/update/', views.ProfileUpdate.as_view(), name='profile_update'),

    path('exercises/',views.myApi, name='the_api'),
    ]

