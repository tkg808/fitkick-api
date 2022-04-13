from rest_framework import serializers
from .models import Workout, Exercise

class ExerciseSerializer(serializers.ModelSerializer):
  exercise_url = serializers.ModelSerializer.serializer_url_field(
    view_name = 'exercise_detail',
  )
    
  owner = serializers.ReadOnlyField(
    source = 'owner.username',
  )

  class Meta:
    model = Exercise
    fields = ('id', 'name', 'notes', 'exercise_url', 'owner')


# Handles how exercises render in workouts.
class NestedExerciseSerializer(serializers.PrimaryKeyRelatedField):

    class Meta:
        model = Exercise

    def to_representation(self, value):
        return value.name


class WorkoutSerializer(serializers.HyperlinkedModelSerializer):
  workout_url = serializers.ModelSerializer.serializer_url_field(
    view_name = 'workout_detail',
  )
  
  exercises = NestedExerciseSerializer(
    many = True,
    queryset = Exercise.objects.all(),
  )

  owner = serializers.ReadOnlyField(
    source = 'owner.username',
  )

  class Meta:
    model = Workout
    fields = ('id', 'name', 'notes', 'exercises', 'workout_url', 'owner')