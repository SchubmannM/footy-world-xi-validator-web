import logging
from typing import List

from footy_validator.dataclasses import UserSubmissionData
from footy_validator.dataclasses import UserSubmissionValidation

logger = logging.getLogger(__name__)


def validate_user_submission(
    user_submission: UserSubmissionData,
) -> List[UserSubmissionValidation]:
    submitted_players = user_submission.players
    validations: List[UserSubmissionValidation] = list()
    temp_club_teams = dict()
    temp_national_teams = dict()

    for player in submitted_players:
        for club_team in player.club_teams:
            if club_team.name in temp_club_teams.keys():
                club_team = temp_club_teams[club_team.name]
            else:
                temp_club_teams[club_team.name] = club_team
            if (
                player not in club_team.players
            ):  # Handles cases where a player comes back from a loan
                club_team.players.append(player)

        for national_team in player.national_teams:
            if national_team.name in temp_national_teams.keys():
                national_team = temp_national_teams[national_team.name]
            else:
                temp_national_teams[national_team.name] = national_team
            national_team.players.append(player)

    for club in temp_club_teams.values():
        if len(club.players) > 1:
            validations.append(
                UserSubmissionValidation(
                    team=club,
                    players=sorted(club.players, key=lambda player: player.full_name),
                )
            )
    for club in temp_national_teams.values():
        if len(club.players) > 1:
            validations.append(
                UserSubmissionValidation(
                    team=club,
                    players=sorted(club.players, key=lambda player: player.full_name),
                )
            )

    return validations
