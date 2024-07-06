# Generated by Django 5.0.6 on 2024-07-06 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_alter_tracker_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracker',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='repository_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='project',
            name='repository_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='repository_token',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='repository_type',
            field=models.CharField(blank=True, choices=[('github', 'GitHub'), ('gitlab', 'GitLab'), ('bitbucket', 'Bitbucket')], max_length=10),
        ),
        migrations.AddField(
            model_name='project',
            name='repository_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='tracker_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='project',
            name='tracker_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='tracker_token',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='tracker_type',
            field=models.CharField(blank=True, choices=[('github', 'GitHub'), ('gitlab', 'GitLab'), ('jira', 'Jira')], max_length=10),
        ),
        migrations.AddField(
            model_name='project',
            name='tracker_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.DeleteModel(
            name='Repository',
        ),
        migrations.DeleteModel(
            name='Tracker',
        ),
    ]
