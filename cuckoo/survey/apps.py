from django.apps import AppConfig


class SurveyConfig(AppConfig):

    name = 'survey'

    def ready(self):
        from . import signals
