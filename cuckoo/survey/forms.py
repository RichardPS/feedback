from django import forms
from django.forms import ModelForm, DateInput
from .models import LaunchSurvey
from .models import SupportSurvey
from .models import SupportQuestions

from .config import QUESTION_OPTIONS


class SupportSurveyForm(ModelForm):
    class Meta:
        model = SupportSurvey
        fields = ['domain']


class SupportQuestionsForm(ModelForm):
    class Meta:
        model = SupportQuestions
        fields = ['comment', 'marketing']
        labels = {
            'comment': ('Your Comments'),
            'marketing': ('OK for marketing?')
        }


class LaunchSurveyForm(ModelForm):
    class Meta:
        model = LaunchSurvey
        fields = ['domain', 'advisor', 'sales', 'ordered', 'launched']



class SupportOptionsForm(forms.Form):
    quality = forms.MultipleChoiceField(
            widget = forms.RadioSelect, choices=QUESTION_OPTIONS
        )
    speed = forms.MultipleChoiceField(
            widget = forms.RadioSelect, choices=QUESTION_OPTIONS
        )
    service = forms.MultipleChoiceField(
            widget = forms.RadioSelect, choices=QUESTION_OPTIONS
        )
