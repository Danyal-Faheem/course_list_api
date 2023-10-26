from rest_framework.generics import ListAPIView
from lms.djangoapps.course_api.serializers import CourseSerializer
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from rest_framework.filters import SearchFilter

class CourseListFilterAPIView(ListAPIView):
    """
    View to list all available courses and filter them according to name and language
    Utilizes the builtin openedx CourseOverview model and CourseSerializer
    Using SearchFilter to allow filtering
    """
    serializer_class = CourseSerializer
    queryset = CourseOverview.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['language', 'display_name']