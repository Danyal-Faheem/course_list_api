"""
URLs for task1.
"""
from django.urls import path
from task1.views import CourseListAPIView

urlpatterns = [
    path('v1/courses/', CourseListAPIView.as_view(), name='course_list')
]
