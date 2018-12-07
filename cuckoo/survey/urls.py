from django.conf.urls import url, handler404

from . import views

urlpatterns = [
    # SUPPORT URLS
    url(
        r'^create/support/$',
        views.create_support_survey,
        name='create_support_survey'
        ),
    url(r'^survey/support/(?P<uuid>[a-f0-9]+)$',
        views.complete_support_survey,
        name='complete_support_survey'
        ),
    url(r'^admin/support/$',
        views.view_support_surverys,
        name='view_support_surverys'
        ),
    url(r'^admin/all-support/$',
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
        ),
    # LAUNCH URLS
    url(r'^create/launch/$',
        views.create_launch_survey,
        name='create_launch_survey'
        ),
    url(r'^survey/launch/(?P<uuid>[a-f0-9]+)$',
        views.complete_launch_survey,
        name='complete_launch_survey'
        ),
    url(r'^admin/launch/$',
        views.view_launch_surveys,
        name='view_launch_surveys'
        ),
    url(r'^admin/all-launch/$',
        views.view_all_launch_surveys,
        name='view_all_launch_surveys'
        ),
    url(r'^json/launch/(?P<startdate>\d{4}-\d{2}-\d{2})/(?P<enddate>\d{4}-\d{2}-\d{2})/$',
        views.json_launch,
        name='json_launch'
        )
]
