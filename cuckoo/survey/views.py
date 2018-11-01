from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404

import pdb

from .forms import SupportOptionsForm
from .forms import SupportSurveyForm
from .forms import SupportQuestionsForm
from .models import SupportSurvey
from .models import SupportQuestions


# Create your views here.
@login_required
def create_support_survey(request):
    """ create support survey form """
    page_name = "Create Support Survey"
    if request.method == 'POST':
        create_support_survey_form = SupportSurveyForm(request.POST)
        regarding = request.POST.get("regarding").split(",")
        # pdb.set_trace()
        if create_support_survey_form.is_valid() and len(regarding) == 7:
            survey = create_support_survey_form.save(commit=False)
            survey.price = regarding[0]
            survey.details = regarding[1]
            survey.completed_by = regarding[2]
            survey.time = regarding[3]
            survey.checked_by = regarding[4]
            survey.set_up_by = regarding[5]
            
            survey.save()

            messages.success(request, "Success")
            messages.info(request, "{0}/support-survey/{1}".format(
                request.META['HTTP_HOST'],
                survey.uuid)
            )

            # pdb.set_trace()

            return redirect('/create-support-survey/')
        else:
            messages.error(request, "Invalid Data")
    else:
        create_support_survey_form = SupportSurveyForm()
    return render(
        request,
        'survey/create_support_survey.html',
        {
            'page_name': page_name,
            'create_support_survey_form': create_support_survey_form,
        }
        )


def complete_support_survey(request, uuid):
    """ create feedback form """
    if request.method == 'POST':
        support_survey = SupportSurvey.objects.get(uuid=uuid)
        support_feedback_form = SupportQuestionsForm(request.POST)
        support_options_form = SupportOptionsForm(request.POST)
        if support_feedback_form.is_valid():
            # pdb.set_trace()
            questions = support_feedback_form.save(commit=False)
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
        support_feedback_form = SupportQuestionsForm()
        support_options_form = SupportOptionsForm()
    return render(
        request,
        'survey/support_feedback_form.html',
        {
            'support_feedback_form': support_feedback_form,
            'support_options_form': support_options_form
        }
        )

def survey_success(request):
    return render(
        request,
        'survey/survey-success.html',
        {}
        )

def view_support_surverys(request):
    """ admin view all surveys """
    all_support_feedback = SupportSurvey.objects.all()
    # pdb.set_trace()
    return render(
        request,
        'survey/view-support-surverys.html',
        {
            'all_support_feedback': all_support_feedback
        }
        )
