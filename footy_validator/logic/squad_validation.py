import logging
from typing import List

from footy_validator.dataclasses import FootballPlayerData
from footy_validator.dataclasses import UserSubmissionValidation
from footy_validator.models import FootballPlayer
from footy_validator.models import UserSubmission

logger = logging.getLogger(__name__)


def validate_user_submission(
    user_submission: UserSubmission,
) -> List[UserSubmissionValidation]:
    """
    Go over all submitted players and check if any of them played for one and the same team.
    The teams of the players are added to lists and then for every new player we check if
    one of the teams the player played for is already in the list.
    If so we make a query to find out which players played for this team - this is purely to give
    the user additional information on why their submission is invalid.
    TODO: This can be refactored to get some performance improvements in the future.
    """
    submitted_players = user_submission.players.all()
    all_club_teams = list()
    all_national_teams = list()
    validations: List[UserSubmissionValidation] = list()
    for player_instance in submitted_players:
        player = FootballPlayerData.from_instance(player_instance)
        validation = UserSubmissionValidation(player=player, reasons_incorrect=[])
        teams_played_for = player.club_teams
        for team in teams_played_for:
            if team.name not in all_club_teams:
                all_club_teams.append(team.name)
            else:
                other_players_in_that_team = FootballPlayer.objects.filter(
                    club_teams__name=team.name, user_submissions__id=user_submission.id
                ).exclude(full_name=player.full_name)
                if other_players_in_that_team:
                    validation.reasons_incorrect.append(
                        f" played for {team.name}. {', '.join(player.full_name for player in other_players_in_that_team)} also played there."
                    )

        national_teams_played_for = player.national_teams
        for national_team in national_teams_played_for:
            if national_team.name not in all_national_teams:
                all_national_teams.append(national_team.name)
            else:
                other_players_in_that_team = FootballPlayer.objects.filter(
                    national_teams__name=national_team.name,
                    user_submissions__id=user_submission.id,
                ).exclude(full_name=player.full_name)
                if other_players_in_that_team:
                    validation.reasons_incorrect.append(
                        f" played for {national_team.name}. {', '.join(player.full_name for player in other_players_in_that_team)} also played there."
                    )
        validations.append(validation)
    return validations
