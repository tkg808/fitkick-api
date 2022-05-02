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
    # GET localhost:8000/exercises-info
    # POST localhost:8000/exercises-info
    path('exercise-infos/', views.ExerciseInfoList.as_view(), name = 'exercise_info_list'),
    # # PUT localhost:8000/exercise-infos/:id
    path('exercise-infos/<int:pk>', views.ExerciseInfoDetail.as_view(), name = 'exercise_info_detail'),
    # GET localhost:8000/events
    # POST localhost:8000/events
    path('events/', views.EventList.as_view(), name = 'event_list'),
    # # PUT localhost:8000/events/:id
    path('events/<int:pk>', views.EventDetail.as_view(), name = 'event_detail'),
]