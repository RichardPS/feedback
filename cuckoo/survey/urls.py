from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^create-support-survey/$',
        views.create_support_survey,
        name='create_support_survey'
        ),
    url(r'^support-survey/(?P<pk>\w+)$',
        views.complete_support_survey,
        name='complete_support_survey'
        )
]
