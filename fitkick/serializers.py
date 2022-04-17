from rest_framework import serializers
from .models import Workout, Exercise, ExerciseInfo


class ExerciseInfoSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(
    source = "owner.username",
  )

  exercise = serializers.ReadOnlyField(
    source = "exercise.name",
  )

  # owner = serializers.PrimaryKeyRelatedField()

  # exercise = serializers.PrimaryKeyRelatedField()

  notes = serializers.CharField(allow_blank = True)

  class Meta:
    model = ExerciseInfo
    fields = ('id', 'notes', 'exercise', 'owner')

  # # Overriding behavior due to nesting.
  # def create(self, validated_data):
  #   # Separate model data.
  #   exercise_info_data = validated_data.pop('exercise_info')
  #   # Create Exercise with validated_data.
  #   exercise_data = Exercise.objects.create(**validated_data)
  #   # Create ExerciseInfo with popped validated_data.
  #   # Have to specify exercise_info_owner.
  #   ExerciseInfo.objects.create(
  #     # Connects new ExerciseInfo to the recently created Exercise.
  #     exercise = exercise_data,
  #     # Field has to be a User instance.
  #     owner = validated_data['owner'],
  #     **exercise_info_data)
  #   return exercise_data

  # def update(self, instance, validated_data):
  #   # Separate model data.
  #   exercise_info_data = validated_data.pop('exercise_info')

  #   # 1 update Exercise instance => save
  #   instance.name = validated_data.get('name', instance.name)
  #   instance.exercise_type = validated_data.get('exercise_type', instance.exercise_type)
  #   instance.primary_muscles = validated_data.get('primary_muscles', instance.primary_muscles)
  #   instance.secondary_muscles = validated_data.get('secondary_muscles', instance.secondary_muscles)
  #   instance.save()
  
  #   # Creates if new, updates otherwise.
  #   # Returns a tuple => data, boolean.
  #   # Boolean is True if created, False if fetched.
  #   exercise_info, created = ExerciseInfo.objects.get_or_create(
  #     # Fields to evaluate for similarity.
  #     # Does not enforce uniqueness
  #     exercise = instance.name,
  #     owner = instance.owner,
  #     # Fields to use if create is necessary.
  #     defaults = {'notes': exercise_info_data.notes}
  #     )

  #   # 5 return instance


class ExerciseSerializer(serializers.ModelSerializer):
  exercise_url = serializers.ModelSerializer.serializer_url_field(
    view_name = 'exercise_detail',
  )
    
  owner = serializers.ReadOnlyField(
    source = 'owner.username',
  )

  # There are many exercise_info, but a user can only use their own.
  # exercise_info = ExerciseInfo.objects.get_or_create(
  #     # Fields to evaluate for similarity.
  #     # Does not enforce uniqueness
  #     exercise_id = ExerciseInfo.objects.filter,
  #     owner_id = 'user.id',
  #     # Fields to use if create is necessary.
  #     defaults = {'notes': ""}
  #     )

  # There are many exercise_info, but a user can only use their own.
  exercise_info = ExerciseInfoSerializer(
    # many = True,
    # required = True,
    # queryset = ExerciseInfo.objects.all(),
  )

  class Meta:
    model = Exercise
    fields = ('id', 'name', 'exercise_type', 'primary_muscles', 'secondary_muscles', 'exercise_url', 'owner', 'exercise_info')


  # Overriding behavior due to nesting.
  def create(self, validated_data):
    # Separate model data.
    exercise_info_data = validated_data.pop('exercise_info')
    # Create Exercise with validated_data.
    exercise_data = Exercise.objects.create(**validated_data)
    # Create ExerciseInfo with popped validated_data.
    # Have to specify owner for exercise_info.
    ExerciseInfo.objects.create(
      # Connects new ExerciseInfo to the recently created Exercise.
      exercise = exercise_data,
      # Field has to be a User instance.
      owner = validated_data['owner'],
      notes = exercise_info_data['notes'],
      )
    return exercise_data

  def update(self, instance, validated_data):
    # Separate model data.
    exercise_info_data = validated_data.pop('exercise_info')

    # 1 update Exercise instance => save
    instance.name = validated_data.get('name', instance.name)
    instance.exercise_type = validated_data.get('exercise_type', instance.exercise_type)
    instance.primary_muscles = validated_data.get('primary_muscles', instance.primary_muscles)
    instance.secondary_muscles = validated_data.get('secondary_muscles', instance.secondary_muscles)
    instance.save()
  
    # Creates if new, updates otherwise.
    # Returns a tuple => data, boolean.
    # Boolean is True if created, False if fetched.
    exercise_info, created = ExerciseInfo.objects.get_or_create(
      # Fields to evaluate for similarity.
      # Does not enforce uniqueness
      exercise = instance.name,
      owner = instance.owner,
      # Fields to use if create is necessary.
      defaults = {'notes': exercise_info_data[0][notes]}
      )

    # 5 return instance


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