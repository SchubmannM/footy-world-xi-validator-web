from dataclasses import dataclass
from dataclasses import field
from typing import List
from typing import Optional

from .models import ClubTeam
from .models import FootballPlayer
from .models import NationalTeam
from .models import UserSubmission


@dataclass(eq=False)
class Team:
    name: str
    players: List["FootballPlayerData"] = field(default_factory=list)
    team_picture_url: Optional[str] = None

    def __eq__(self, other):
        return self.name == other.name


class ClubTeamData(Team):
    def to_instance(self) -> ClubTeam:
        team, _ = ClubTeam.objects.update_or_create(
            name=self.name, defaults={"team_picture_url": self.team_picture_url}
        )
        return team


class NationalTeamData(Team):
    def to_instance(self) -> NationalTeam:
        team, _ = NationalTeam.objects.update_or_create(
            name=self.name, defaults={"team_picture_url": self.team_picture_url}
        )
        return team


@dataclass
class FootballPlayerData:
    player_instance: Optional[FootballPlayer]
    full_name: Optional[str]
    birthday: Optional[str]
    alias: Optional[str]
    profile_picture_url: Optional[str]
    profile_url: Optional[str]

    club_teams: List[ClubTeamData] = field(default_factory=list)
    national_teams: List[NationalTeamData] = field(default_factory=list)

    def to_instance(self) -> FootballPlayer:
        player, created = FootballPlayer.objects.get_or_create(
            full_name=self.full_name,
            profile_picture_url=self.profile_picture_url,
            profile_url=self.profile_picture_url,
        )
        if created:
            club_teams = [team.to_instance() for team in self.club_teams]
            national_teams = [team.to_instance() for team in self.national_teams]
            player.club_teams.add(*club_teams)
            player.national_teams.add(*national_teams)
        return player


@dataclass
class UserSubmissionValidation:
    team: Team
    players: List["FootballPlayerData"]


@dataclass
class UserSubmissionData:
    players: List[FootballPlayerData] = field(default_factory=list)

    def to_instance(self) -> UserSubmission:
        user_submission_instance = UserSubmission.objects.create()
        for player in self.players:
            if player.player_instance:
                user_submission_instance.players.add(player.player_instance)
            else:
                player_instance = player.to_instance()
                user_submission_instance.players.add(player_instance)
        user_submission_instance = UserSubmission.validate(user_submission_instance)
        return user_submission_instance
