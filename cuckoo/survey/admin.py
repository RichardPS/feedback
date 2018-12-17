from django.contrib import admin

# Register your models here.
from .models import SupportSurvey, SupportQuestions
from .models import LaunchSurvey, LaunchQuestions


class SupportSurveyAdmin(admin.ModelAdmin):
    readonly_fields = ['created']


class SupportQuestionsAdmin(admin.ModelAdmin):
    readonly_fields = ['date_submitted']


class LaunchQuestionsAdmin(admin.ModelAdmin):
    readonly_fields = ['date_submitted']


admin.site.register(SupportSurvey, SupportSurveyAdmin)
admin.site.register(SupportQuestions, SupportQuestionsAdmin)
admin.site.register(LaunchSurvey)
admin.site.register(LaunchQuestions, LaunchQuestionsAdmin)
