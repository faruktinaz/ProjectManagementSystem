# Generated by Django 5.0.6 on 2024-07-06 10:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_tracker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='repositories', to='projects.project'),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trackers', to='projects.project'),
        ),
    ]
