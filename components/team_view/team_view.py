from django_components import component

from footy_validator.models import TemporarySubmissionPlayers
from footy_validator.models import TemporaryUserSubmission
from footy_validator.utils import get_players_from_request


@component.register("team_view")
class TeamView(
    component.Component,
):
    template_name = "team_view/team_view.html"

    def get_context_data(self):
        request = self.outer_context.get("request")  # type: ignore
        players = get_players_from_request(request)
        return {
            "players": players,
        }

    class Media:
        css = "team_view/team_view.css"
        js = "team_view/team_view.js"
