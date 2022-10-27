from uuid import UUID

from crispy_forms.layout import Submit
from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.views.generic import DetailView

from .dataclasses import FootballPlayerData, UserSubmissionData
from .forms import FootballPlayerForm, FootballPlayerFormSetHelper
from .logic.get_player_from_transfermarkt import get_player_search_result
from .models import (
    FootballPlayer,
    TemporarySubmissionPlayers,
    TemporaryUserSubmission,
    UserSubmission,
)


def index(request):
    if request.session.get("temp_submission_id", None):
        temp_submission, created = TemporaryUserSubmission.objects.get_or_create(
            id=request.session["temp_submission_id"]
        )
    else:
        temp_submission = TemporaryUserSubmission.objects.create()
        request.session["temp_submission_id"] = str(temp_submission.id)
    players = (
        TemporarySubmissionPlayers.objects.filter(temp_user_submission=temp_submission)
        .order_by("-created")
        .values("player__full_name", "player__id", "player__profile_picture_url")
    )
    return render(request, "index.html", {"players": players})


class UserSubmissionView(DetailView):
    queryset = UserSubmission.objects.all()
    template_name = "submission_detail.html"
    pk_url_kwarg = "id"
    context_object_name = "submission"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
