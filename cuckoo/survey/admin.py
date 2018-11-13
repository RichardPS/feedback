from django.contrib import admin

# Register your models here.
from .models import SupportSurvey, SupportQuestions
from .models import LaunchSurvey, LaunchQuestions

admin.site.register(SupportSurvey)
admin.site.register(SupportQuestions)
admin.site.register(LaunchSurvey)
admin.site.register(LaunchQuestions)
