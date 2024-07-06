from django.db import models

# add new projects with details such as name, slug, description, and language.
class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    language = models.CharField(max_length=50)
    
    repository_title = models.CharField(max_length=100, blank=True)
    repository_url = models.CharField(max_length=255, blank=True)
    REPOSITORY_TYPES = [
        ('github', 'GitHub'), ('gitlab', 'GitLab'), ('bitbucket', 'Bitbucket')
    ]
    repository_type = models.CharField(choices=REPOSITORY_TYPES, max_length=10, blank=True)
    repository_email = models.EmailField(blank=True)
    repository_token = models.CharField(max_length=255, blank=True)
    
    tracker_title = models.CharField(max_length=100, blank=True)
    tracker_url = models.CharField(max_length=255, blank=True)
    TRACKER_TYPES = [
        ('github', 'GitHub'), ('gitlab', 'GitLab'), ('jira', 'Jira'),
    ]
    tracker_type = models.CharField(choices=TRACKER_TYPES, max_length=10, blank=True)
    tracker_email = models.EmailField(blank=True)
    tracker_token = models.CharField(max_length=255, blank=True)

    def _str_(self):
        return self.name