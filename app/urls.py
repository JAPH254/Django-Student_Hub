#urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('student', StudentViewSet, basename='student')
router.register('course', CourseViewSet, basename='course')
router.register('announcement', AnnouncementViewSet, basename='announcement')
router.register('assignment', AssignmentViewSet, basename='assignment')
router.register('librarybook', LibraryBookViewSet, basename='librarybook')
urlpatterns = [
    path('', include(router.urls)),
]