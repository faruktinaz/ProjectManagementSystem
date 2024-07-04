from django.db import models

# add new projects with details such as name, slug, description, and language.
class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    language = models.CharField(max_length=50)