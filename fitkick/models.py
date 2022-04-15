from django.db import models
from django.contrib.postgres.fields import ArrayField

# Allows user ownership over these fields.
class ExerciseInfo(models.Model):
  notes = models.TextField(blank = True)
  # Stores reps and weights as pairs.
  # Set number for reps/weights handled in UI.
  sets = ArrayField(
    ArrayField(
      models.PositiveSmallIntegerField(),
      size = 2,
    ))

  exercise_info_owner = models.ForeignKey(
    'users.User', 
    related_name = 'exercise_infos',
    on_delete = models.CASCADE,
    )

  # Inherited so it won't generate it's own table.
  class Meta:
    abstract = True

  def __str__(self):
    return self.name

class Exercise(ExerciseInfo):
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
  notes = models.TextField(blank = True)

  exercise_owner = models.ForeignKey(
    'users.User', 
    related_name = 'exercises',
    on_delete = models.CASCADE,
    )

  def __str__(self):
    return self.name


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

  def __str__(self):
    return self.name


