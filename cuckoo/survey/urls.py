from django.conf.urls import url
from django.conf.urls import handler404

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
    url(r'^view-all-support-surverys/$',
        views.view_all_support_surveys,
        name='view_all_support_surveys'
        ),
    url(r'^json/support/(?P<startdate>\d{4}-\d{2}-\d{2})/(?P<enddate>\d{4}-\d{2}-\d{2})/$',
        views.json_support,
        name='json_support'
        ),
    url(r'^survey-success/$',
        views.survey_success,
        name='survey_success'
        )
]
handler404 = 'survey.views.error_404'
