""""
Careful: name 'apps' but already in apps 'blog' scope in this file
its a configuration file actually
"""

from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
