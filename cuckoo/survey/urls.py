from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^create-support-survey/$',
        views.create_support_survey,
        name='create_support_survey'
        ),
    url(r'^support-survey/(?P<uuid>\S+)$',
        views.complete_support_survey,
        name='complete_support_survey'
        ),
    url(r'^view-support-surverys/$',
        views.view_support_surverys,
        name='view_support_surverys'
        ),
    url(r'^survey-success/$',
        views.survey_success,
        name='survey_success'
        )
]
