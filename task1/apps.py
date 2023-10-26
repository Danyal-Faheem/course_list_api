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

    # Class attribute that configures and enables this app as a Plugin App.
    plugin_app = {
        # Configuration setting for Plugin URLs for this app.
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                # The namespace to provide to django's urls.include.
                PluginURLs.NAMESPACE: 'task1',

                # The application namespace to provide to django's urls.include.
                # Optional; Defaults to None.
                PluginURLs.APP_NAME: 'task1',

                # The regex to provide to django's urls.url.
                # Optional; Defaults to r''.
                PluginURLs.REGEX: r'^api/task1/',

                # The python path (relative to this app) to the URLs module to be plugged into the project.
                # Optional; Defaults to 'urls'.
                PluginURLs.RELATIVE_PATH: 'urls',
            },
        },

    }
