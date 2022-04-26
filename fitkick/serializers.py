from rest_framework import serializers
from .models import Workout, Exercise, ExerciseInfo


class ExerciseInfoSerializer(serializers.ModelSerializer):
  exercise_info_url = serializers.ModelSerializer.serializer_url_field(
    view_name = 'exercise_info_detail',
  )

  notes = serializers.CharField(
    allow_blank = True,
    required = False,
    allow_null = True,
    )

  exercise_id = serializers.IntegerField(
    required = True,
  )

  exercise_name = serializers.ReadOnlyField(
    source = 'exercise.name',
  )

  class Meta:
    model = ExerciseInfo
    fields = ('id', 'notes', 'exercise_id', 'exercise_name', 'owner_id', 'exercise_info_url')


class ExerciseSerializer(serializers.ModelSerializer):
  exercise_url = serializers.ModelSerializer.serializer_url_field(
    view_name = 'exercise_detail',
  )
    
  owner = serializers.ReadOnlyField(
    source = 'owner.username',
  )

  class Meta:
    model = Exercise
    fields = ('id', 'name', 'exercise_type', 'primary_muscles', 'secondary_muscles', 'exercise_url', 'owner', 'owner_id')
    

# Lets me see a list of all exercises.
class NestedExerciseSerializer(serializers.PrimaryKeyRelatedField):

  class Meta:
    model = Exercise
    # fields = ('name')

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
  workout_url = serializers.ModelSerializer.serializer_url_field(
    view_name = 'workout_detail',
  )
  
  owner = serializers.ReadOnlyField(
    source = 'owner.username',
  )
  
  exercises = NestedExerciseSerializer(
    many = True,
    required = False,
    queryset = Exercise.objects.all(),
  )

  class Meta:
    model = Workout
    fields = ('id', 'name', 'notes', 'exercises', 'workout_url', 'owner')