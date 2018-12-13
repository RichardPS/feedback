from django.db.models.signals import post_save
from django.dispatch import receiver

from .functions import quality_alert_check
from .models import SupportQuestions
from .models import LaunchQuestions


@receiver(post_save, sender=SupportQuestions)
def support_question_saved(sender, instance, **kwargs):
    created = kwargs.get('created', False)
    if not created:
        return

    survey = instance.support_survey
    scores_list = {
                'Quality': questions.quality,
                'Speed': questions.speed,
                'Service': questions.service,
            }
    department = 'support'
    quality_alert_check(
                support_survey.domain,
                scores_list,
                department,
                support_survey.uuid,
                )


@receiver(post_save, sender=LaunchQuestions)
def launch_question_saved(sender, instance, **kwargs):
    created = kwargs.get('created', False)
    if not created:
        return

    survey = instance.launch_survey

    scores_list = {
        'Quality': questions.quality,
        'Speed': questions.speed,
        'Service': questions.service,
        'Training': questions.training,
        }
    department = 'launch'
    quality_alert_check(
        launch_survey.domain,
        scores_list,
        department,
        launch_survey.uuid,
        )
