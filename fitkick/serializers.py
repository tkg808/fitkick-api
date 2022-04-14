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


# Handles how exercises are serialized in workouts.
class NestedExerciseSerializer(serializers.PrimaryKeyRelatedField):

  class Meta:
    model = Exercise
    fields = ('name')

  # Only serializes the exercise's name.
  def to_representation(self, obj):
    return obj.name

  # Uses exercise name to find exercise and update list.
  def to_internal_value(self, data):
    
    # data variable should be the name of the exercise (type string).
    if not data:
      raise serializers.ValidationError({
        'name': 'This field is required',
        })
    if not (isinstance (data, str)):
      raise serializers.ValidationError("Expecting exercise's name")

    # Finds the exercise.
    obj = Exercise.objects.filter(name=data).values()[0]

    # Unlikely outcome.
    if not obj:
      raise serializers.ValidationError("No exercise with that name.")

    return obj['id']


class WorkoutSerializer(serializers.HyperlinkedModelSerializer):
  # def update(self, instance, validated_data):
  #   instance.name = validated_data.get('name', instance.name)
  #   instance.notes = validated_data.get('notes', instance.notes)
  #   instance.save()
  #   return instance

  workout_url = serializers.ModelSerializer.serializer_url_field(
    view_name = 'workout_detail',
  )
  
  exercises = NestedExerciseSerializer(
    many = True,
    required = False,
    queryset = Exercise.objects.all(),
  )

  # exercises = ExerciseSerializer(
  #   many = True,
  # )

  owner = serializers.ReadOnlyField(
    source = 'owner.username',
  )

  class Meta:
    model = Workout
    fields = ('id', 'name', 'notes', 'exercises', 'workout_url', 'owner')