from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, RepositoryViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('repositories', RepositoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]