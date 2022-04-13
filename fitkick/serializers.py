from rest_framework import serializers
from .models import Workout, Exercise

class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
  exercise_url = serializers.ModelSerializer.serializer_url_field(
    view_name = 'exercise_detail',
  )
    
  owner = serializers.ReadOnlyField(
    source = 'owner.username',
  )

  class Meta:
    model = Exercise
    fields = ('id', 'name', 'notes', 'exercise_url', 'owner')


class WorkoutSerializer(serializers.HyperlinkedModelSerializer):
  workout_url = serializers.ModelSerializer.serializer_url_field(
    view_name = 'workout_detail',
  )
  
  exercises = ExerciseSerializer(
    many = True,
  )

  owner = serializers.ReadOnlyField(
    source = 'owner.username',
  )

  class Meta:
    model = Workout
    fields = ('id', 'name', 'notes', 'exercises', 'workout_url', 'owner')