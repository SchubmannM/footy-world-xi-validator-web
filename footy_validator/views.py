from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView
from django_htmx.http import trigger_client_event

from footy_validator.logic.get_player_from_transfermarkt import get_player_from_url
from footy_validator.models import TemporarySubmissionPlayers
from footy_validator.models import TemporaryUserSubmission
from footy_validator.models import UserSubmission
from footy_validator.utils import get_players_from_request
from footy_validator.utils import get_temp_team_id_from_session


def index(request):
    temp_submission_id = request.session.get("temp_submission_id", None)
    temp_submission, _ = TemporaryUserSubmission.objects.get_or_create(
        id=temp_submission_id
    )
    request.session["temp_submission_id"] = str(temp_submission.id)
    return TemplateResponse(request, "index.html", {})


class UserSubmissionView(DetailView):
    queryset = UserSubmission.objects.all()
    template_name = "submission_detail.html"
    pk_url_kwarg = "id"
    context_object_name = "submission"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@require_http_methods(["GET", "POST", "DELETE"])
def football_team_view(request):
    if request.method == "GET":
        players = get_players_from_request(request)
        context = {"players": players}
        return TemplateResponse(request, "team_view/_players.html", context)
    if request.method == "POST":
        response = HttpResponse()
        temp_team_id = get_temp_team_id_from_session(request)
        player_url = request.POST.get("playerUrl")
        temp_submission = TemporaryUserSubmission.objects.get(id=temp_team_id)
        player = get_player_from_url(player_url)
        if not player:
            return HttpResponse(503)
        player_instance = player.to_instance()
        TemporarySubmissionPlayers.objects.get_or_create(
            temp_user_submission=temp_submission, player=player_instance
        )
        response = HttpResponse()
        trigger_client_event(
            response,
            "football-team-updated",
            {},
        )
        return response
    if request.method == "DELETE":
        temp_team_id = get_temp_team_id_from_session(request)
        player_id = request.htmx.trigger.split("_")[1]
        TemporarySubmissionPlayers.objects.filter(
            temp_user_submission_id=temp_team_id, player_id=player_id
        ).delete()
        response = HttpResponse()
        trigger_client_event(
            response,
            "football-team-updated",
            {},
        )
        return response
