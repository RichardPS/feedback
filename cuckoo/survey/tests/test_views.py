from survey.views import survey_success
from survey.config import FEEDBACK_THANKYOU_MESSAGE

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
