"""
task1 Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import (
    PluginURLs
)

from openedx.core.djangoapps.plugins.constants import ProjectType

class Task1Config(AppConfig):
    """
    Configuration for the task1 Django application.
    """

    name = 'task1'
    
    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
               PluginURLs.NAMESPACE: 'task1',
                PluginURLs.REGEX: r'^api/task1/',
                PluginURLs.RELATIVE_PATH: 'urls',
            },
        },
    }