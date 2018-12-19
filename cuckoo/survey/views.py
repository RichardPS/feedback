from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render, redirect

import pdb  # noqa: F401

from .forms import DateFilter
from .forms import LaunchSurveyForm
from .forms import SupportSurveyForm
from .forms import SupportQuestionsForm
from .forms import LaunchQuestionsForm

from .models import LaunchSurvey
from .models import LaunchQuestions
from .models import SupportSurvey
from .models import SupportQuestions

from .config import FEEDBACK_THANKYOU_MESSAGE
from .config import PAGE_NOT_FOUND
from .config import SUPPORT_INTRO_TEXT
from .config import LAUNCH_INTRO_TEXT

from .functions import convert_str_to_date
from .functions import get_questions_form


# 404 Page.
def page_not_found(request):
    response = render(
        request,
        'survey/404.html',
        )
    response.status_code = PAGE_NOT_FOUND
    return response

def admin_area(
        request,
        template_name='survey/admin_area.html'):

    context = {}

    return render (
        request,
        template_name,
        context
        )

# SUPPORT VIEWS
@login_required()
def create_support_survey(
        request,
        template_name='survey/create_support_survey.html'):
    """ create support survey form """
    page_name = "Create Support Survey"
    if request.method == 'POST':
        create_support_survey_form = SupportSurveyForm(request.POST)

        if create_support_survey_form.is_valid():

            survey = create_support_survey_form.save()

            messages.success(request, "Success")
            messages.info(request, "{0}/survey/support/{1}".format(
                request.META['HTTP_HOST'],
                survey.uuid)
            )

            return redirect('/create/support/')
        else:
            messages.error(request, "Invalid Data")
    else:
        create_support_survey_form = SupportSurveyForm()

    context = {
        'page_name': page_name,
        'create_support_survey_form': create_support_survey_form,
        }
    return render(
        request,
        template_name,
        context
        )


def complete_support_survey(
        request,
        uuid,
        template_name='survey/feedback_form.html'):
    """ create feedback form """
    intro_text = SUPPORT_INTRO_TEXT
    if request.method == 'POST':
        support_survey = SupportSurvey.objects.get(uuid=uuid)
        feedback_form = SupportQuestionsForm(request.POST)
        options_form = get_questions_form('support')(request.POST)
        if feedback_form.is_valid():
            questions = feedback_form.save(commit=False)
            questions.support_survey = support_survey
            questions.quality = request.POST.get("quality")
            questions.speed = request.POST.get("speed")
            questions.service = request.POST.get("service")

            questions.save()
            messages.success(request, "Success")
            return redirect('/survey-success/')
        else:
            messages.error(request, "Invalid Data")

    else:
        feedback_form = SupportQuestionsForm()
        options_form = get_questions_form('support')

    context = {
        'intro_text': intro_text,
        'feedback_form': feedback_form,
        'options_form': options_form
        }
    return render(
        request,
        template_name,
        context
        )


def survey_success(
        request,
        template_name='survey/survey-success.html'):
    """ survey succes page """
    feedback_thankyou_message = FEEDBACK_THANKYOU_MESSAGE

    context = {
        'feedback_thankyou_message': feedback_thankyou_message,
        }
    return render(
        request,
        template_name,
        context
        )


@staff_member_required()
def view_support_surverys(
        request,
        template_name='survey/view-support-surverys.html'):
    """ admin view first surveys """
    all_support_feedback = SupportQuestions.objects.all()
    all_support_feedback = all_support_feedback.distinct('support_survey')
    view_all = False

    startdate = request.GET.get('startdate')
    enddate = request.GET.get('enddate')

    if startdate:
        all_support_feedback = all_support_feedback.filter(
            date_submitted__range=(startdate, enddate))

    datefilter_form = DateFilter()

    context = {
        'all_support_feedback': all_support_feedback,
        'view_all': view_all,
        'datefilter_form': datefilter_form
    }
    return render(
        request,
        template_name,
        context
        )


@staff_member_required()
def view_all_support_surveys(
        request,
        template_name='survey/view-support-surverys.html'):
    """ admin view all surveys """
    all_support_feedback = SupportQuestions.objects.all()
    view_all = True

    startdate = request.GET.get('startdate')
    enddate = request.GET.get('enddate')

    if startdate:
        all_support_feedback = all_support_feedback.filter(
            date_submitted__range=(startdate, enddate))

    datefilter_form = DateFilter()

    context = {
        'all_support_feedback': all_support_feedback,
        'view_all': view_all,
        'datefilter_form': datefilter_form
        }
    return render(
        request,
        template_name,
        context
        )


@staff_member_required()
def view_support_survey(
        request,
        uuid,
        template_name='survey/view_support_survey.html'):

    survey = SupportSurvey.objects.get(uuid=uuid)
    feedback = survey.supportquestions_set.all()
    # pdb.set_trace()
    context = {
        'survey': survey,
        'feedback': feedback
        }

    return render(
        request,
        template_name,
        context
        )


def json_support(
        request,
        startdate,
        enddate):
    """ admin view first surveys as json """
    startdate = convert_str_to_date(startdate)
    enddate = convert_str_to_date(enddate)

    all_support_feedback = SupportQuestions.objects.filter(
        date_submitted__range=(
            startdate,
            enddate
            )
        ).distinct('support_survey')

    json_data = serialize('json', all_support_feedback)

    return HttpResponse(json_data, content_type='application/json')


@login_required()
def create_launch_survey(
        request,
        template_name='survey/create_launch_survey.html'):
    """ create launch survey """
    if request.method == 'POST':
        create_launch_survey_form = LaunchSurveyForm(request.POST)
        if create_launch_survey_form.is_valid():
            survey = create_launch_survey_form.save()

            messages.success(request, "Success")
            messages.info(request, "{0}/survey/launch/{1}".format(
                request.META['HTTP_HOST'],
                survey.uuid)
            )

            return redirect('/create/launch/')
        else:
            messages.error(request, "Invalid Data")
    else:
        create_launch_survey_form = LaunchSurveyForm()

    context = {'create_launch_survey_form': create_launch_survey_form}

    return render(
        request,
        template_name,
        context
        )


def complete_launch_survey(
        request,
        uuid,
        template_name='survey/feedback_form.html'):
    """ create feedback form """
    intro_text = LAUNCH_INTRO_TEXT

    if request.method == 'POST':
        launch_survey = LaunchSurvey.objects.get(uuid=uuid)
        feedback_form = LaunchQuestionsForm(request.POST)
        options_form = get_questions_form('launch')(request.POST)
        if feedback_form.is_valid():
            questions = feedback_form.save(commit=False)
            questions.launch_survey = launch_survey
            questions.quality = request.POST.get("quality")
            questions.speed = request.POST.get("speed")
            questions.service = request.POST.get("service")
            questions.training = request.POST.get("training")

            questions.save()
            messages.success(request, "Success")
            return redirect('/survey-success/')
        else:
            messages.error(request, "Invalid Data")
    else:
        feedback_form = LaunchQuestionsForm()
        options_form = get_questions_form('launch')

    context = {
        'intro_text': intro_text,
        'feedback_form': feedback_form,
        'options_form': options_form
        }

    return render(
        request,
        template_name,
        context
        )


@staff_member_required()
def view_launch_surveys(
        request,
        template_name='survey/view-launch-surverys.html'):
    """ admin view first surveys """
    all_launch_feedback = LaunchQuestions.objects.all()
    all_launch_feedback = all_launch_feedback.distinct('launch_survey')
    view_all = False

    startdate = request.GET.get('startdate')
    enddate = request.GET.get('enddate')

    if startdate:
        all_launch_feedback = all_launch_feedback.filter(
            date_submitted__range=(startdate, enddate))

    datefilter_form = DateFilter()

    context = {
        'all_launch_feedback': all_launch_feedback,
        'view_all': view_all,
        'datefilter_form': datefilter_form
        }
    return render(
        request,
        template_name,
        context
        )


@staff_member_required()
def view_all_launch_surveys(
        request,
        template_name='survey/view-launch-surverys.html'):
    """ admin view all surveys """
    all_launch_feedback = LaunchQuestions.objects.all()
    view_all = True

    startdate = request.GET.get('startdate')
    enddate = request.GET.get('enddate')

    if startdate:
        all_launch_feedback = all_launch_feedback.filter(
            date_submitted__range=(startdate, enddate))

    datefilter_form = DateFilter()

    context = {
        'all_launch_feedback': all_launch_feedback,
        'view_all': view_all,
        'datefilter_form': datefilter_form
        }
    return render(
        request,
        template_name,
        context
        )


@staff_member_required()
def view_launch_survey(
        request,
        uuid,
        template_name='survey/view-launch-survey.html'):

    survey = LaunchSurvey.objects.get(uuid=uuid)
    feedback = survey.launchquestions_set.all()

    context = {
        'survey': survey,
        'feedback': feedback
        }

    return render(
        request,
        template_name,
        context
        )


def json_launch(
        request,
        startdate,
        enddate):
    """ admin view first surveys as json """
    startdate = convert_str_to_date(startdate)
    enddate = convert_str_to_date(enddate)

    all_launch_feedback = LaunchQuestions.objects.filter(
        date_submitted__range=(
            startdate,
            enddate
            )
        ).distinct('launch_survey')

    json_data = serialize('json', all_launch_feedback)

    return HttpResponse(json_data, content_type='application/json')
