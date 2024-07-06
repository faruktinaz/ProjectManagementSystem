# Generated by Django 5.0.6 on 2024-07-05 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_repository'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='add_repository',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='token',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.CharField(blank=True, choices=[('github', 'GitHub'), ('gitlab', 'GitLab'), ('bitbucket', 'Bitbucket')], max_length=10),
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.DeleteModel(
            name='Repository',
        ),
    ]
