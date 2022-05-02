from rest_framework import generics, views, permissions
from .models import Workout, Exercise, ExerciseInfo, Event
from .serializers import WorkoutSerializer, ExerciseSerializer, ExerciseInfoSerializer, EventSerializer
from .permissions import IsOwnerOrReadOnly


# Workout => GET, POST
class WorkoutList(generics.ListCreateAPIView):
  # Model to use to list/create.
  queryset = Workout.objects.all()
  # Defines how data is sent back and forth as json.
  serializer_class = WorkoutSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  # Overwrite the perform_create method.
  def perform_create(self, serializer):
    # Sets owner field automatically.
    serializer.save(owner = self.request.user)

# Workout => SHOW, UPDATE, DELETE
class WorkoutDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Workout.objects.all()
  serializer_class = WorkoutSerializer
  permission_classes = [IsOwnerOrReadOnly]


# Exercise => GET, POST
class ExerciseList(generics.ListCreateAPIView):
  queryset = Exercise.objects.all()
  serializer_class = ExerciseSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(owner = self.request.user)

# Exercise => SHOW, UPDATE, DELETE
class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Exercise.objects.all()
  serializer_class = ExerciseSerializer
  permission_classes = [IsOwnerOrReadOnly]


# ExerciseInfo => GET, POST
class ExerciseInfoList(generics.ListCreateAPIView):
  serializer_class = ExerciseInfoSerializer
  permission_classes = [permissions.IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(owner = self.request.user)

  # Only gets the user's exercise info
  def get_queryset(self):
    return ExerciseInfo.objects.filter(owner = self.request.user)

# ExerciseInfo => SHOW, UPDATE
class ExerciseInfoDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = ExerciseInfo.objects.all()
  serializer_class = ExerciseInfoSerializer
  permission_classes = [IsOwnerOrReadOnly]


# Event => GET, POST
class EventList(generics.ListCreateAPIView):
  serializer_class = EventSerializer
  permission_classes = [permissions.IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(owner = self.request.user)

  def get_queryset(self):
    return Event.objects.filter(owner = self.request.user)

# Event => SHOW, UPDATE, DELETE
class EventDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer
  permission_classes = [IsOwnerOrReadOnly]
