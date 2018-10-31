from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

import pdb

from .forms import SupportSurveyForm
from .forms import SupportQuestionsForm
from .models import SupportSurvey
from .models import SupportQuestions


# Create your views here.
@login_required
def create_support_survey(request):
    """ create support survey form """
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
            # pdb.set_trace()
            survey.save()
            messages.success(request, "Success")
            return redirect('/create-support-survey/')
        else:
            messages.error(request, "Invalid Data")
    else:
        create_support_survey_form = SupportSurveyForm()
    return render(
        request,
        'survey/create_support_survey.html',
        {
            'create_support_survey_form': create_support_survey_form
        }
        )


def complete_support_survey(request, pk):
    """ create feedback form """
    if request.method == 'POST':
        support_survey = SupportSurvey.objects.get(pk=pk)
        support_feedback_form = SupportQuestionsForm(request.POST)
        if support_feedback_form.is_valid():
            questions = support_feedback_form.save(commit=False)
            questions.support_survey = support_survey
            questions.quality = request.POST.get("quality")
            questions.speed = request.POST.get("speed")
            questions.service = request.POST.get("service")

            # pdb.set_trace()
            questions.save()
            messages.success(request, "Success")
            return redirect('/survey_success/')
        else:
            messages.error(request, "Invalid Data")
    else:
        support_feedback_form = SupportQuestionsForm()
    return render(
        request,
        'survey/support_feedback_form.html',
        {
            'support_feedback_form': support_feedback_form
        }
        )
