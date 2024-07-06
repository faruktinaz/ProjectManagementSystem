from rest_framework import serializers
from .models import Project, Repository

class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = '__all__'
        
class ProjectSerializer(serializers.ModelSerializer):
    repositories = RepositorySerializer(many=True)
    class Meta:
        model = Project
        fields = '__all__'