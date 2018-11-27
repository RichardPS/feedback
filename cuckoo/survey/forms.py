from django import forms
from django.forms import ModelForm, SelectDateWidget
from django.forms.widgets import TextInput
from .models import LaunchSurvey
from .models import LaunchQuestions
from .models import SupportSurvey
from .models import SupportQuestions

from .config import SUPPORT_LABELS
from .config import LAUNCH_LABELS
from .config import QUESTION_OPTIONS


class MyDateInput(TextInput):
    input_type = 'date'

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


class LaunchQuestionsForm(ModelForm):
    class Meta:
        model = LaunchQuestions
        fields = ['comment', 'marketing']
        labels = {
            'comment': ('Your Comments'),
            'marketing': ('OK for marketing?')
        }


class LaunchSurveyForm(ModelForm):
    """ widget overrides """
    def __init__(self, *args, **kwargs):
        super(LaunchSurveyForm, self).__init__(*args, **kwargs)
        self.fields['ordered'].widget = MyDateInput(attrs={'class':'date'})
        self.fields['launched'].widget = MyDateInput(attrs={'class':'date'})

    class Meta:
        model = LaunchSurvey
        fields = ['domain', 'advisor', 'sales', 'ordered', 'launched']


class SupportOptionsForm(forms.Form):
    quality = forms.MultipleChoiceField(
            widget = forms.RadioSelect,
            choices=QUESTION_OPTIONS,
            label=SUPPORT_LABELS['quality']
        )
    speed = forms.MultipleChoiceField(
            widget = forms.RadioSelect,
            choices=QUESTION_OPTIONS,
            label=SUPPORT_LABELS['speed']
        )
    service = forms.MultipleChoiceField(
            widget = forms.RadioSelect,
            choices=QUESTION_OPTIONS,
            label=SUPPORT_LABELS['service']
        )


class LaunchOptionsForm(forms.Form):
    quality = forms.MultipleChoiceField(
            widget = forms.RadioSelect,
            choices=QUESTION_OPTIONS,
            label=LAUNCH_LABELS['quality']
        )
    speed = forms.MultipleChoiceField(
            widget = forms.RadioSelect,
            choices=QUESTION_OPTIONS,
            label=LAUNCH_LABELS['speed']
        )
    service = forms.MultipleChoiceField(
            widget = forms.RadioSelect,
            choices=QUESTION_OPTIONS,
            label=LAUNCH_LABELS['service']
        )
    training = forms.MultipleChoiceField(
            widget = forms.RadioSelect,
            choices=QUESTION_OPTIONS,
            label=LAUNCH_LABELS['training']
        )


FORM_TYPES = {
    'support': SupportOptionsForm,
    'launch': LaunchOptionsForm,
}
