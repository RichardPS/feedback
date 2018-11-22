from django.core.mail import send_mail
from .config import EMAIL_CONTACTS

from datetime import datetime
import pdb

from .forms import FORM_TYPES

def url_check(url):
    """ adds http to url if not present """
    PREFIX_STRING = "http://"
    start_of_url = url[0:4]

    if start_of_url != "http":
        url = PREFIX_STRING + url

    return url


def quality_alert_check(school_domain, school_scores, department):
    """ check is scores are low """
    for score in school_scores:
        if int(score) < 50:
            email_low_score_alert(school_domain, school_scores, department)

    return


def email_low_score_alert(school_domain, school_scores, department):
    """ email manager if scores are low """
    sendto = EMAIL_CONTACTS[department]

    send_mail(
        'Low Score Alert{0}'.format(school_domain),
        'scores go here',
        'test@appletongate.co.uk',
        [sendto],
        fail_silently=False,
        )

    return


def convert_str_to_date(date_str):
    """ convert string date into date """
    format_str = '%Y-%m-%d'
    datetime_object = datetime.strptime(date_str, format_str)

    return datetime_object.date()

def get_questions_form(form_type):
    return FORM_TYPES[form_type]
