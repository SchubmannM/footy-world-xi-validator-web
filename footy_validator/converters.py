from footy_validator import models
from footy_validator.dataclasses import ClubTeamData
from footy_validator.dataclasses import FootballPlayerData
from footy_validator.dataclasses import NationalTeamData
from footy_validator.dataclasses import UserSubmissionData


def convert_national_team(national_team: models.NationalTeam) -> NationalTeamData:
    return NationalTeamData(
        name=national_team.name, team_picture_url=national_team.team_picture_url
    )


def convert_club_team(club_team: models.ClubTeam) -> ClubTeamData:
    return ClubTeamData(
        name=club_team.name, team_picture_url=club_team.team_picture_url
    )


def convert_football_player(
    football_player: models.FootballPlayer,
) -> FootballPlayerData:
    return FootballPlayerData(
        player_instance=football_player,
        full_name=football_player.full_name,
        birthday=None,
        alias=None,
        profile_picture_url=football_player.profile_picture_url,
        profile_url=football_player.profile_url,
        club_teams=[
            convert_club_team(club_team)
            for club_team in football_player.club_teams.all()
        ],
        national_teams=[
            convert_national_team(national_team)
            for national_team in football_player.national_teams.all()
        ],
    )


def convert_user_submission(
    user_submission: models.TemporaryUserSubmission,
) -> UserSubmissionData:
    return UserSubmissionData(
        players=[
            convert_football_player(football_player)
            for football_player in user_submission.players.all()
        ]
    )
