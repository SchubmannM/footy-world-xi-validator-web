from django_components import component

from footy_validator.models import TemporarySubmissionPlayers
from footy_validator.models import TemporaryUserSubmission


@component.register("team_view")
class TeamView(
    component.Component,
):
    template_name = "team_view/team_view.html"

    def get_context_data(self):
        session = self.outer_context.get("request").session
        temp_team_id = session.get("temp_submission_id")
        temp_submission = TemporaryUserSubmission.objects.get(id=temp_team_id)
        players = (
            TemporarySubmissionPlayers.objects.filter(
                temp_user_submission=temp_submission
            )
            .order_by("-created")
            .values("player__full_name", "player__id", "player__profile_picture_url")
        )
        return {
            "players": players,
        }

    class Media:
        css = "team_view/team_view.css"
        js = "team_view/team_view.js"
