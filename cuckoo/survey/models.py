from django.contrib import admin  # noqa: F401
from django.db import models
from django. urls import reverse

import uuid


# SUPPORT MODELS
class SupportSurvey(models.Model):
    """ inital data for support survey """
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
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

    def get_absolute_url(self):
        return reverse(
            'single_survey',
            args=[str(self.uuid)]
            )


class SupportQuestions(models.Model):
    """ questions for support survey """
    support_survey = models.ForeignKey(SupportSurvey, on_delete=models.CASCADE)
    quality = models.DecimalField(max_digits=5, decimal_places=2)
    speed = models.DecimalField(max_digits=5, decimal_places=2)
    service = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.TextField(blank=True)
    marketing = models.BooleanField(default=False)
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0}'.format(self.support_survey.domain)


# LAUNCH MODELS
class LaunchSurvey(models.Model):
    """ inital data for launch survey """
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    domain = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    advisor = models.CharField(max_length=255)
    sales = models.CharField(max_length=255)
    ordered = models.DateField(
        auto_now_add=False,
        auto_now=False,
        blank=False
        )
    launched = models.DateField(
        auto_now_add=False,
        auto_now=False,
        blank=False
        )
    time_to_launch = models.DurationField()

    def __str__(self):
        return '{0}'.format(self.domain)

    def get_absolute_url(self):
        return reverse(
            'single_survey',
            args=[str(self.uuid)]
            )


class LaunchQuestions(models.Model):
    """ questions for launch survey """
    launch_survey = models.ForeignKey(LaunchSurvey, on_delete=models.CASCADE)
    quality = models.DecimalField(max_digits=5, decimal_places=2)
    speed = models.DecimalField(max_digits=5, decimal_places=2)
    service = models.DecimalField(max_digits=5, decimal_places=2)
    training = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.TextField(blank=True)
    marketing = models.BooleanField(default=False)
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0}'.format(self.launch_survey.domain)
