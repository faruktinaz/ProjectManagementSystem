from rest_framework import serializers
from .models import Project, Repository, Tracker

class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = '__all__'
        
class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    repositories = RepositorySerializer(many=True)
    trackers = TrackerSerializer(many=True)
    class Meta:
        model = Project
        fields = '__all__'