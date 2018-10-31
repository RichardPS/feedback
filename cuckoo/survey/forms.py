from django import forms
from django.forms import ModelForm
from .models import SupportSurvey
from .models import SupportQuestions


QUESTION_OPTIONS = (
    ('0', 'Unsatifactory'),
    ('50', 'Satifactory'),
    ('100', 'Excelent'),
    )


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
