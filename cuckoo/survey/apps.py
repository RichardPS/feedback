from django.apps import AppConfig


class SurveyConfig(AppConfig):

    name = 'survey'
    verbose_name = "FEEDBACK SYSTEM"

    def ready(self):
        from . import signals  # noqa: F401
