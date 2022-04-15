from django.db import models

class Exercise(models.Model):
  TYPE_CHOICES = (
    ('Aerobic', 'Aerobic'),
    ('Anaerobic', 'Anaerobic'),
    ('Mobility', 'Mobility'),
  )

  name = models.CharField(max_length = 50)
  exercise_type = models.CharField(
    max_length = 10,
    choices = TYPE_CHOICES,
    default = '',
    )
  notes = models.TextField(blank = True)

  owner = models.ForeignKey(
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


