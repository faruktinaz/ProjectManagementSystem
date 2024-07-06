from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, RepositoryViewSet, TrackerViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('repositories', RepositoryViewSet)
router.register('trackers', TrackerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]