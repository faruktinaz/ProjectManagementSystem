from django.shortcuts import render
from rest_framework import viewsets
from .models import Project, Repository, Tracker
from .serializers import ProjectSerializer, RepositorySerializer, TrackerSerializer

# I learned that I don't need to write separate views for CRUD operations.
# All operations can be done in a single ViewSet.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class RepositoryViewSet(viewsets.ModelViewSet):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer

class TrackerViewSet(viewsets.ModelViewSet):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer