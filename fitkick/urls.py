from django.urls import path, include
from .import views

urlpatterns = [
    # GET localhost:8000/workouts
    # POST localhost:8000/workouts
    path('workouts/', views.WorkoutList.as_view(), name = 'workout_list'),
    # PUT localhost:8000/workouts/:id
    # DELETE localhost:8000/workouts/:id
    path('workouts/<int:pk>', views.WorkoutDetail.as_view(), name = 'workout_detail'),
    # GET localhost:8000/exercises
    # POST localhost:8000/exercises
    path('exercises/', views.ExerciseList.as_view(), name = 'exercise_list'),
    # PUT localhost:8000/exercises/:id
    # DELETE localhost:8000/exercises/:id
    path('exercises/<int:pk>', views.ExerciseDetail.as_view(), name = 'exercise_detail'),
]