from django.apps import AppConfig


class Config(AppConfig):
    name = 'apps.follows'
    label = 'civic_europe_follows'

    def ready(self):
        import apps.follows.signals  # noqa:F401
