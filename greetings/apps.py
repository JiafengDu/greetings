"""
greetings Django application initialization.
"""

from django.apps import AppConfig


class GreetingsConfig(AppConfig):
    """
    Configuration for the greetings Django application.
    """

    name = 'greetings'
    verbose_name = 'Greetings'
    
    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'api',
                'regex': '^api/',
                'relative_path': 'urls',
            }
        },
        'settings_config': {
            'lms.djangoapp': {
                'test': { 'relative_path': 'settings.test' },
                'common': { 'relative_path': 'settings.common' },
            }
        },
    }
