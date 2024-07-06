# Generated by Django 5.0.6 on 2024-07-06 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_repository_email_alter_repository_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='type',
            field=models.CharField(blank=True, choices=[('github', 'GitHub'), ('gitlab', 'GitLab'), ('jira', 'Jira'), ('', '')], max_length=10),
        ),
    ]