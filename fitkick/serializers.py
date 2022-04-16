from rest_framework import serializers
from .models import Workout, Exercise, ExerciseInfo


class ExerciseInfoSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(
    # source = "user.username",
  )

  exercise = serializers.ReadOnlyField(
    # source = 'exercise.name',
  )

  notes = serializers.CharField(
    default = "",
  )

  class Meta:
    model = ExerciseInfo
    fields = ('id', 'notes', 'exercise', 'owner')


class ExerciseSerializer(serializers.ModelSerializer):
  exercise_url = serializers.ModelSerializer.serializer_url_field(
    view_name = 'exercise_detail',
  )
    
  owner = serializers.ReadOnlyField(
    source = 'owner.username',
  )

  exercise_info = ExerciseInfoSerializer(
    required = False,
    # queryset = ExerciseInfo.objects.all(),
  )

  class Meta:
    model = Exercise
    fields = ('id', 'name', 'exercise_type', 'primary_muscles', 'secondary_muscles', 'exercise_url', 'owner', 'exercise_info')

  def create(self, validated_data):
    # Separate model data.
    exercise_info_data = validated_data.pop('exercise_info')
    # Create Exercise with validated_data.
    exercise_data = Exercise.objects.create(**validated_data)
    # Create ExerciseInfo with popped validated_data.
    # Have to specify exercise_info_owner.
    ExerciseInfo.objects.create(
      # Connects new ExerciseInfo to the recently created Exercise.
      exercise = exercise_data,
      owner = validated_data['owner'],
      **exercise_info_data)
    return exercise_data


# Lets me see a list of all exercises.
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