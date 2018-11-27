from survey.functions import convert_str_to_date

from survey.views import survey_success
from survey.views import complete_support_survey
from survey.views import json_support

from survey.config import FEEDBACK_THANKYOU_MESSAGE
from survey.config import SUPPORT_INTRO_TEXT

import datetime

HTTP_OK = 200


def test_survey_success():
    request = None
    response = survey_success(request)
    assert response.status_code == HTTP_OK


def test_survey_success_contains_message():
    request = None
    response = survey_success(request)
    assert str(FEEDBACK_THANKYOU_MESSAGE) in str(response.content)


def test_message_constant():
    expected_value = '<p>Thank you for your feedback</p>'
    assert str(expected_value) == str(FEEDBACK_THANKYOU_MESSAGE)


def test_complete_support_survey_contains_message():
    expected_value = '<p>Some intro blurb for the support feedback form</p>'
    assert str(expected_value) == str(SUPPORT_INTRO_TEXT)


def test_convert_str_to_date():
    string_date_input = "2018-01-31"
    date_object = convert_str_to_date(string_date_input)
    assert isinstance(date_object, datetime.date)
