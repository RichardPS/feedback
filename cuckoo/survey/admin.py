from django.contrib import admin

# Register your models here.
from .models import SupportSurvey, SupportQuestions

admin.site.register(SupportSurvey)
admin.site.register(SupportQuestions)
