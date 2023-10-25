"""
task1 Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import (
    PluginURLs, PluginSettings, PluginContexts
)

class Task1Config(AppConfig):
    """
    Configuration for the task1 Django application.
    """

    name = 'task1'
    
    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'courses',
                'regex': '^api/courses/',
                'relative_path': 'api.urls',
            }
        },
        'settings_config': {
            'lms.djangoapp': {
                'production': { 'relative_path': 'settings.production' },
                'common': { 'relative_path': 'settings.common' },
            }
        },
        'signals_config': {
            'lms.djangoapp': {
                'relative_path': 'my_signals',
                'receivers': [{
                    'receiver_func_name': 'on_signal_x',
                    'signal_path': 'full_path_to_signal_x_module.SignalX',
                    'dispatch_uid': 'courses.my_signals.on_signal_x',
                    'sender_path': 'full_path_to_sender_app.ModelZ',
                }],
            }
        },
        'view_context_config': {
            'lms.djangoapp': {
                'course_dashboard': 'courses.context_api.get_dashboard_context'
            }
        }
    }