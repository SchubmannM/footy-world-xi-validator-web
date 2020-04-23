from uuid import UUID

from crispy_forms.layout import Submit
from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView

from .dataclasses import FootballPlayerData, UserSubmissionData
from .forms import FootballPlayerForm, FootballPlayerFormSetHelper
from .models import FootballPlayer, UserSubmission


def index(request):
    FootballPlayerFormSet = formset_factory(
        FootballPlayerForm, min_num=11, max_num=11, can_delete=False, can_order=False
    )
    helper = FootballPlayerFormSetHelper()
    helper.add_input(Submit("submit", "Validate"))
    if request.method == "POST":
        user_submission: UserSubmissionData = UserSubmissionData()
        formset = FootballPlayerFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                player: FootballPlayerData = form.cleaned_data.get("player")
                user_submission.players.append(player)
            instance = user_submission.to_instance()
            return redirect("user-submission-view", id=instance.id)
    else:
        formset = FootballPlayerFormSet()

    return render(request, "index.html", {"formset": formset, "helper": helper})


class UserSubmissionView(DetailView):
    queryset = UserSubmission.objects.all()
    template_name = "submission_detail.html"
    pk_url_kwarg = "id"
    context_object_name = "submission"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
