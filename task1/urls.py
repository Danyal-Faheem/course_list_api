"""
URLs for task1.
"""
from django.urls import path
from task1.views import CourseListFilterAPIView

urlpatterns = [
    path('list-filter/', CourseListFilterAPIView.as_view(), name='course_list_filter')
]
