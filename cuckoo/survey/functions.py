from django.core.mail import send_mail
from .config import EMAIL_CONTACTS


def url_check(url):

    PREFIX_STRING = "//"

    start_of_url = url[0:4]

    if start_of_url != "http":
        url_check = PREFIX_STRING + url

    return


def quality_alert_check(school_domain, school_scores, department):
    # print(school_domain)
    # print(school_scores)
    # print(department)

    for score in school_scores:
        if int(score) < 50:
            email_low_score_alert(school_domain, school_scores, department)

    return


def email_low_score_alert(school_domain, school_scores, department):

    sendto = EMAIL_CONTACTS[department]
    # print(sendto)
    
    send_mail(
        'Low Score Alert{0}'.format(school_domain),
        'scores go here',
        'test@appletongate.co.uk',
        [sendto],
        fail_silently=False,
        )

    return
