from django.contrib import admin
from django.db import models

# Create your models here.
class SupportSurvey(models.Model):
    """ inital data required for survey """
    domain = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=10)
    details = models.CharField(max_length=255)
    completed_by = models.CharField(max_length=5)
    time = models.CharField(max_length=10)
    checked_by = models.CharField(max_length=5)
    set_up_by = models.CharField(max_length=5)

    def __str__(self):
        return '{0}'.format(self.domain)


class SupportQuestions(models.Model):
    """ Questions for support servey """
    support_survey = models.ForeignKey(SupportSurvey, on_delete=models.CASCADE)
    quality = models.DecimalField(max_digits=5, decimal_places=2)
    speed = models.DecimalField(max_digits=5, decimal_places=2)
    service = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.TextField()
    marketing = models.BooleanField(default=False)
    date_submitted = models.DateTimeField(auto_now_add=True)
