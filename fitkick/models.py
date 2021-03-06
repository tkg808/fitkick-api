from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import date

# Allows notes to be specific to the user.
class ExerciseInfo(models.Model):
  notes = models.TextField(null = True)

  # One User, Many ExerciseInfo.
  owner = models.ForeignKey(
    'users.User', 
    related_name = 'exercise_infos',
    on_delete = models.CASCADE,
    )

  # One Exercise, Many ExerciseInfo.
  exercise = models.ForeignKey(
    'Exercise',
    related_name = 'exercise_infos',
    on_delete = models.CASCADE,
  )

  class Meta:
    # Acts as a surrogate primary key column.
    unique_together = (("owner", "exercise"),)


class Exercise(models.Model):
  TYPE_CHOICES = (
    ('Aerobic', 'Aerobic'),
    ('Anaerobic', 'Anaerobic'),
    ('Mobility', 'Mobility'),
  )

  MUSCLE_CHOICES = (
    ('Legs', 'Legs'),
    ('Back', 'Back'),
    ('Chest', 'Chest'),
    ('Shoulders', 'Shoulders'),
    ('Arms', 'Arms'),
    ('Core', 'Core'),
    ('Cardio', 'Cardio'),
    ('None', 'None'),
  )

  name = models.CharField(max_length = 50)

  exercise_type = models.CharField(
    max_length = 10,
    choices = TYPE_CHOICES,
    default = '',
    )
    
  primary_muscles = models.CharField(
    max_length = 10,
    choices = MUSCLE_CHOICES,
    default = '',
  )

  secondary_muscles = models.CharField(
    max_length = 10,
    choices = MUSCLE_CHOICES,
    default = '',
  )

  owner = models.ForeignKey(
    'users.User', 
    related_name = 'exercises',
    on_delete = models.CASCADE,
    )


class Workout(models.Model):
  name = models.CharField(max_length = 50, blank = True)
  notes = models.TextField(blank = True)
  
  exercises = models.ManyToManyField(
    Exercise,
    related_name = 'workouts',
    blank = True,
  )

  owner = models.ForeignKey(
    'users.User', 
    related_name = 'workouts',
    on_delete = models.CASCADE,
    )


class Event(models.Model):
  title = models.CharField(max_length = 50, blank = False)
  
  # One Workout, Many Events
  workout = models.ForeignKey(
    Workout,
    related_name = 'events',
    on_delete = models.CASCADE,
  )

  # One Owner, Many Events
  owner = models.ForeignKey(
    'users.User',
    related_name = 'events',
    on_delete = models.CASCADE,
  )

  date = models.DateField()