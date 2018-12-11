from django.core.mail import send_mail
from .config import EMAIL_CONTACTS

from datetime import datetime
import pdb  # noqa: F401

from .forms import FORM_TYPES


def quality_alert_check(school_domain, school_scores, department, uuid):
    """ check is scores are low """
    email_call = False
    for score in school_scores:
        if int(school_scores[score]) < 50:
            email_call = True

    if email_call:
        email_low_score_alert(school_domain, school_scores, department, uuid)

    return


def email_low_score_alert(school_domain, school_scores, department, uuid):
    """ email manager if scores are low """
    subject = 'Low {0} score alert {1}'.format(department, school_domain)
    message = ""
    for score in school_scores:
        message = message + "{0}: {1}\n".format(
            score,
            school_scores[score],
            )

    message = message + "\nAdd url here with direct link {0}\n".format(uuid)

    sender = 'feedback@primarysite.net'
    sendto = EMAIL_CONTACTS[department]

    send_mail(
        subject,
        message,
        sender,
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
