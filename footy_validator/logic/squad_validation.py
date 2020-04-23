import logging
from typing import List, Optional

from footy_validator.models import UserSubmission, FootballPlayer
from footy_validator.dataclasses import UserSubmissionValidation

logger = logging.getLogger(__name__)


def validate_user_submission(
    user_submission: UserSubmission,
) -> UserSubmissionValidation:
    submitted_players = user_submission.players.all()
    all_club_teams = list()
    all_national_teams = list()
    validations = list()
    for player in submitted_players:
        teams_played_for = player.club_teams.all()
        for team in teams_played_for:
            if team.name not in all_club_teams:
                all_club_teams.append(team.name)
            else:
                other_players_in_that_team = FootballPlayer.objects.filter(
                    club_teams__name=team.name, user_submissions__id=user_submission.id
                ).exclude(full_name=player.full_name)
                if other_players_in_that_team:
                    validations.append(
                        UserSubmissionValidation(
                            reason_incorrect=f"{player.full_name} played for {team.name}. {', '.join(player.full_name for player in other_players_in_that_team)} also played there."
                        )
                    )

        national_teams_played_for = player.national_teams.all()
        for national_team in national_teams_played_for:
            if national_team.name not in all_national_teams:
                all_national_teams.append(national_team.name)
            else:
                other_players_in_that_team = FootballPlayer.objects.filter(
                    national_teams__name=national_team.name,
                    user_submissions__id=user_submission.id,
                ).exclude(full_name=player.full_name)
                if other_players_in_that_team:
                    validations.append(
                        UserSubmissionValidation(
                            reason_incorrect=f"{player.full_name} played for {national_team.name}. {', '.join(player.full_name for player in other_players_in_that_team)} also played there."
                        )
                    )
    return validations
