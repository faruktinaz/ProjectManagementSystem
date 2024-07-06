from django.db import models

# add new projects with details such as name, slug, description, and language.
class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    language = models.CharField(max_length=50)
    
class Repository(models.Model):
    TYPES = [
		('github', 'GitHub'), ('gitlab','GitLab'), ('bitbucket','Bitbucket')
	]
    project = models.ForeignKey(Project, related_name='repositories', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField()
    type = models.CharField(choices=TYPES, max_length=10)
    email = models.EmailField()
    token = models.CharField()
