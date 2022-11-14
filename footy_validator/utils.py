from typing import Any
from typing import Dict
from typing import List

from django.http import HttpRequest

from footy_validator.models import TemporarySubmissionPlayers


def get_temp_team_id_from_session(request):
    return request.session.get("temp_submission_id")


def get_players_from_request(request: HttpRequest) -> List[Dict[str, Any]]:
    temp_submission_id = get_temp_team_id_from_session(request)
    players = (
        TemporarySubmissionPlayers.objects.filter(
            temp_user_submission_id=temp_submission_id
        )
        .order_by("-created")
        .values("player__full_name", "player__id", "player__profile_picture_url")
    )
    return list(players)
