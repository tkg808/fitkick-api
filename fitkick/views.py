from rest_framework import generics, permissions
from .models import Workout, Exercise, ExerciseInfo
from .serializers import WorkoutSerializer, ExerciseSerializer, ExerciseInfoSerializer
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
# class ExerciseInfoList(generics.ListCreateAPIView):
#   queryset = ExerciseInfo.objects.all()
#   serializer_class = ExerciseInfoSerializer
#   permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#   def perform_create(self, serializer):
#     serializer.save(owner = self.request.user)

# # ExerciseInfo => SHOW, UPDATE
# class ExerciseInfoDetail(generics.RetrieveUpdateDestroyAPIView):
#   queryset = ExerciseInfo.objects.all()
#   serializer_class = ExerciseInfoSerializer
#   permission_classes = [IsOwnerOrReadOnly]