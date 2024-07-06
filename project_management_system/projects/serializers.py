from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        repository_title = validated_data.pop('repository_title', None)
        repository_url = validated_data.pop('repository_url', None)
        repository_type = validated_data.pop('repository_type', None)
        repository_email = validated_data.pop('repository_email', None)
        repository_token = validated_data.pop('repository_token', None)

        tracker_title = validated_data.pop('tracker_title', None)
        tracker_url = validated_data.pop('tracker_url', None)
        tracker_type = validated_data.pop('tracker_type', None)
        tracker_email = validated_data.pop('tracker_email', None)
        tracker_token = validated_data.pop('tracker_token', None)

        project_detail = Project.objects.create(
            **validated_data,
            repository_title=repository_title,
            repository_url=repository_url,
            repository_type=repository_type,
            repository_email=repository_email,
            repository_token=repository_token,
            tracker_title=tracker_title,
            tracker_url=tracker_url,
            tracker_type=tracker_type,
            tracker_email=tracker_email,
            tracker_token=tracker_token,
        )
        return project_detail

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.description = validated_data.get('description', instance.description)
        instance.language = validated_data.get('language', instance.language)

        instance.repository_title = validated_data.get('repository_title', instance.repository_title)
        instance.repository_url = validated_data.get('repository_url', instance.repository_url)
        instance.repository_type = validated_data.get('repository_type', instance.repository_type)
        instance.repository_email = validated_data.get('repository_email', instance.repository_email)
        instance.repository_token = validated_data.get('repository_token', instance.repository_token)

        instance.tracker_title = validated_data.get('tracker_title', instance.tracker_title)
        instance.tracker_url = validated_data.get('tracker_url', instance.tracker_url)
        instance.tracker_type = validated_data.get('tracker_type', instance.tracker_type)
        instance.tracker_email = validated_data.get('tracker_email', instance.tracker_email)
        instance.tracker_token = validated_data.get('tracker_token', instance.tracker_token)

        instance.save()
        return instance