from django.shortcuts import render
from django.test import RequestFactory

from survey.functions import convert_str_to_date

from survey.forms import get_launch_delta
from survey.forms import SupportSurveyForm

from survey.models import SupportSurvey

from survey.views import survey_success
from survey.views import complete_support_survey
from survey.views import create_support_survey
from survey.views import json_support

from survey.config import FEEDBACK_THANKYOU_MESSAGE
from survey.config import SUPPORT_INTRO_TEXT

import datetime
import pytest
import uuid

HTTP_OK = 200


# ---------------------------------
""" test constants in config.py """
def test_message_constant():
    expected_value = '<p>Thank you for your feedback</p>'
    assert str(expected_value) == str(FEEDBACK_THANKYOU_MESSAGE)


def test_complete_support_survey_contains_message():
    expected_value = '<p>Some intro blurb for the support feedback form</p>'
    assert str(expected_value) == str(SUPPORT_INTRO_TEXT)


# ------------------------------------
""" test functions in functions.py """
def test_convert_str_to_date():
    string_date_input = "2018-01-31"
    date_object = convert_str_to_date(string_date_input)
    assert isinstance(date_object, datetime.date)


def test_get_launch_delta():
    expected_delta = datetime.timedelta(days=3)
    test_start_date = datetime.date.today()
    test_end_date = test_start_date + expected_delta
    delta_result = get_launch_delta(test_start_date, test_end_date)
    assert delta_result == expected_delta


# ----------------------------
""" test views in views.py """
def test_survey_success():
    """ test http response """
    request = None
    response = survey_success(request)
    assert response.status_code == HTTP_OK


def test_survey_success_contains_message():
    """ test response contains message """
    request = None
    response = survey_success(request)
    assert str(FEEDBACK_THANKYOU_MESSAGE) in str(response.content)


# ---------------------
""" test support form view """
""" mock forms """
def _create_support_survey(data=None, form_class=SupportSurveyForm):
    if not data:
        return None, form_class()

    form = form_class(data)

    if form.is_valid():
        survey = form.save()
        return True, survey
    return False, form


def create_support_survey(
    request,
    formhandler=_create_support_survey,
    template_name='survey/create_support_survey.html',
    page_name="Create Support Survey"):

    status, survey = formhandler(request.POST)

    if status is True:
        messages.success(request, "Success")
        messages.info(request, "{0}/survey/support/{1}".format(
            request.META['HTTP_HOST'],
            survey.uuid)
            )
        return redirect('/create/support/')

    if status is False:
        messages.error(request, "Invalid data")

    context = {
        'page_name': page_name,
        'create_support_survey_form': survey,
        }
    return render(request, template_name, context)


# -----------
""" TESTS """

class SimpleObject(object):
    pass

def func_none(data):
    return None, SupportSurveyForm()

def func_false(data):
    return False, SupportSurveyForm()

def func_true(data):
    instance = SimpleObject()
    instance.uuid = uuid.uuid4()
    return True, instance

def test_form_default():
    request = RequestFactory().get('/')
    response = create_support_survey(request, formhandler=func_none)
    assert response.status_code == HTTP_OK

def test_formhandler_empty():
    post = {}
    form_class = SupportSurveyForm
    status, response = _create_support_survey(post)
    assert status is None
    assert response.is_bound is False
    assert isinstance(response, form_class)

def test_formhandler_fail():
    post = {
        'domain': '',
        'regarding': ''
    }
    form_class = SupportSurveyForm
    status, response = _create_support_survey(post)
    assert status is False
    assert response.is_bound is True
    assert isinstance(response, form_class)

@pytest.mark.django_db
def test_formhandler_success():
    post = {
        'domain': 'www.domain.com',
        'regarding': '£0, details, RW, 10, PS, KH, 0'
    }
    form_class = SupportSurveyForm
    status, response = _create_support_survey(post)
    assert status is True
    assert isinstance(response, SupportSurvey)
