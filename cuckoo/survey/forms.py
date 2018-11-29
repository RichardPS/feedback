from django import forms
from django.forms import ModelForm
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


class SupportSurveyForm(forms.Form):
    domain = forms.CharField()
    regarding = forms.CharField()

    _model = SupportSurvey

    def __init__(self, *args, **kwargs):
        self._data = {}
        super(SupportSurveyForm, self).__init__(*args, **kwargs)

    def clean_regarding(self):
        data = self.cleaned_data['regarding']
        regarding = data.split(',')
        if not len(regarding) == 7:
            raise forms.ValidationError('Incorrect number of regarding parameters')

        self._data['price'] = regarding[0]
        self._data['details'] = regarding[1]
        self._data['completed_by'] = regarding[2]
        self._data['time'] = regarding[3]
        self._data['checked_by'] = regarding[4]
        self._data['set_up_by'] = regarding[5]

        return data

    def clean_domain(self):
        data = self.cleaned_data['domain']
        self._data['domain'] = url_check(data)

        return data

    def save(self, commit=True):
        instance = self._model(**self._data)
        if commit:
            instance.save()

        return instance


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
        self.fields['ordered'].widget = MyDateInput(attrs={'class': 'date'})
        self.fields['launched'].widget = MyDateInput(attrs={'class': 'date'})

    class Meta:
        model = LaunchSurvey
        fields = ['domain', 'advisor', 'sales', 'ordered', 'launched']


class SupportOptionsForm(forms.Form):
    quality = forms.MultipleChoiceField(
            widget=forms.RadioSelect,
            choices=QUESTION_OPTIONS,
            label=SUPPORT_LABELS['quality']
        )
    speed = forms.MultipleChoiceField(
            widget=forms.RadioSelect,
            choices=QUESTION_OPTIONS,
            label=SUPPORT_LABELS['speed']
        )
    service = forms.MultipleChoiceField(
            widget=forms.RadioSelect,
            choices=QUESTION_OPTIONS,
            label=SUPPORT_LABELS['service']
        )


class LaunchOptionsForm(forms.Form):
    quality = forms.MultipleChoiceField(
            widget=forms.RadioSelect,
            choices=QUESTION_OPTIONS,
            label=LAUNCH_LABELS['quality']
        )
    speed = forms.MultipleChoiceField(
            widget=forms.RadioSelect,
            choices=QUESTION_OPTIONS,
            label=LAUNCH_LABELS['speed']
        )
    service = forms.MultipleChoiceField(
            widget=forms.RadioSelect,
            choices=QUESTION_OPTIONS,
            label=LAUNCH_LABELS['service']
        )
    training = forms.MultipleChoiceField(
            widget=forms.RadioSelect,
            choices=QUESTION_OPTIONS,
            label=LAUNCH_LABELS['training']
        )


FORM_TYPES = {
    'support': SupportOptionsForm,
    'launch': LaunchOptionsForm,
}


def url_check(url):
    """ adds http to url if not present """
    PREFIX_STRING = "http://"
    start_of_url = url[0:4]

    if start_of_url != "http":
        url = PREFIX_STRING + url

    return url
